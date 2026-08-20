import { cpSync, existsSync, mkdirSync, readdirSync, rmSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();
const output = join(root, "dist");

const rootAssets = [
  "index.html",
  "404.html",
  "robots.txt",
  "sitemap.xml",
  "llms.txt",
  "_headers",
  "_redirects"
];

const excludedDirectories = new Set([
  ".git",
  ".wrangler",
  "__pycache__",
  "dist",
  "node_modules",
  "preview-homes"
]);

rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });

for (const filename of rootAssets) {
  const source = join(root, filename);
  if (!existsSync(source)) {
    throw new Error(`Required deploy asset is missing: ${filename}`);
  }
  cpSync(source, join(output, filename));
}

for (const entry of readdirSync(root, { withFileTypes: true })) {
  if (!entry.isDirectory() || excludedDirectories.has(entry.name)) {
    continue;
  }

  cpSync(join(root, entry.name), join(output, entry.name), {
    recursive: true
  });
}

console.log("Prepared Cloudflare Pages output in dist/.");
