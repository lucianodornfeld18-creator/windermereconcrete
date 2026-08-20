const MAX_FORM_BYTES = 24_000;

const LIMITS = {
  name: 100,
  phone: 40,
  email: 254,
  service: 120,
  city: 120,
  message: 3_000,
};

function isAllowedOrigin(origin) {
  if (!origin) return true;

  try {
    const { hostname, protocol } = new URL(origin);
    if (protocol !== "https:" && hostname !== "localhost" && hostname !== "127.0.0.1") {
      return false;
    }

    return (
      hostname === "windermereconcrete.com" ||
      hostname === "www.windermereconcrete.com" ||
      hostname === "windermereconcrete.pages.dev" ||
      hostname.endsWith(".windermereconcrete.pages.dev") ||
      hostname === "localhost" ||
      hostname === "127.0.0.1"
    );
  } catch {
    return false;
  }
}

function field(form, name) {
  const value = form.get(name);
  return typeof value === "string" ? value.trim() : "";
}

function validate(payload) {
  if (!payload.name || payload.name.length > LIMITS.name) return "Please enter a valid name.";
  if (!payload.phone || payload.phone.length > LIMITS.phone) return "Please enter a valid phone number.";
  if (
    !payload.email ||
    payload.email.length > LIMITS.email ||
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(payload.email)
  ) {
    return "Please enter a valid email address.";
  }
  if (payload.service.length > LIMITS.service) return "Please select a valid service.";
  if (payload.city.length > LIMITS.city) return "Please select a valid city.";
  if (payload.message.length > LIMITS.message) return "The project description is too long.";
  return null;
}

function textResponse(message, status) {
  return new Response(message, {
    status,
    headers: {
      "content-type": "text/plain; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}

export async function onRequestPost(context) {
  const { request, env } = context;
  const contentLength = Number(request.headers.get("content-length") || "0");

  if (contentLength > MAX_FORM_BYTES) {
    return textResponse("This request is too large.", 413);
  }

  if (!isAllowedOrigin(request.headers.get("origin"))) {
    return textResponse("This form submission is not allowed.", 403);
  }

  const contentType = request.headers.get("content-type") || "";
  if (
    !contentType.startsWith("application/x-www-form-urlencoded") &&
    !contentType.startsWith("multipart/form-data")
  ) {
    return textResponse("Unsupported form format.", 415);
  }

  let form;
  try {
    form = await request.formData();
  } catch {
    return textResponse("The form could not be read.", 400);
  }

  if (field(form, "company")) {
    return Response.redirect(new URL("/thanks/", request.url), 303);
  }

  const payload = {
    name: field(form, "name"),
    phone: field(form, "phone"),
    email: field(form, "email"),
    service: field(form, "service"),
    city: field(form, "city"),
    message: field(form, "message"),
    submittedAt: new Date().toISOString(),
  };

  const error = validate(payload);
  if (error) return textResponse(error, 400);

  try {
    const result = await env.CONTACT_EMAIL.fetch("https://contact-email.internal/send", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!result.ok) {
      console.error("Contact email service rejected the submission", {
        status: result.status,
      });
      return textResponse("We could not send your request. Please call (689) 407-6658.", 502);
    }
  } catch (error) {
    console.error("Contact email service was unavailable", {
      name: error instanceof Error ? error.name : "UnknownError",
    });
    return textResponse("We could not send your request. Please call (689) 407-6658.", 502);
  }

  return Response.redirect(new URL("/thanks/", request.url), 303);
}
