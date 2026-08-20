#!/usr/bin/env python3
"""Windermere Concrete — full site build. Run: py build_all.py"""
import time

t0 = time.time()
import _build_home
import _build_services
import _build_cities
import _build_blog
import _build_pages
import _build_sitemap

_build_home.build_home()
_build_services.build_all()
_build_cities.build_all()
_build_blog.build_all()
_build_pages.build_all()
_build_sitemap.build_all()

print(f"\nBUILD COMPLETE in {time.time() - t0:.1f}s")
