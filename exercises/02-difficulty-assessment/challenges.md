# Software Development Challenges

This document contains 18 software development challenges spanning a wide range of complexity levels. Your task is to assess and rank these challenges by difficulty.

**Instructions for students:**
1. Read through all challenge descriptions
2. Use the rubric in `rubric.md` to evaluate each challenge
3. Rank them from simplest to most complex
4. Discuss your rankings with your AI agent
5. Reflect on which challenges are most suitable for AI-assisted development

---

## Challenge 1: Command-Line Calculator

Build a calculator that accepts mathematical expressions via command line and returns the result.

**Domain:** CLI Utility
**Requirements:** Parse and evaluate expressions with basic operators (+, -, *, /, parentheses), handle order of operations, provide clear error messages for invalid input.

---

## Challenge 2: Personal Journal with Search

Create a command-line personal journal application where users can write entries, tag them, and search through past entries.

**Domain:** CLI Application, Data Storage
**Requirements:** Add/edit/delete entries, tag entries, full-text search, date-based filtering, persist data to disk, handle concurrent access.

---

## Challenge 3: Real-Time Chat Application

Build a web-based chat application supporting multiple rooms and user presence indicators.

**Domain:** Web Application, Real-Time Communication
**Requirements:** User authentication, multiple chat rooms, real-time message delivery, user presence (online/offline), message history, deploy to hosting platform.

---

## Challenge 4: URL Shortener Service

Create a URL shortening service similar to bit.ly with a web interface and API.

**Domain:** Web Service, API
**Requirements:** Shorten URLs with custom or generated slugs, redirect service, usage analytics (click count), REST API, web UI, database persistence, handle high traffic.

---

## Challenge 5: Markdown Blog Generator

Build a static site generator that converts markdown files into a complete blog website.

**Domain:** Static Site Generator, File Processing
**Requirements:** Parse markdown to HTML, support posts and pages, generate index/archive pages, templating system, RSS feed, tags/categories, responsive design.

---

## Challenge 6: Task Scheduler with Dependencies

Create a task scheduling system that executes tasks based on schedules and dependency graphs.

**Domain:** Systems Programming, Scheduling
**Requirements:** Cron-like scheduling, task dependencies (task B runs after task A completes), parallel execution where possible, logging, error handling and retries, web UI for monitoring.

---

## Challenge 7: Image Filter Application

Build a desktop application that applies various filters and transformations to images.

**Domain:** Desktop GUI, Image Processing
**Requirements:** Load/save images, filters (blur, sharpen, edge detection, color adjustments), undo/redo, batch processing, preview before applying, native GUI (not web-based).

---

## Challenge 8: Recipe Search and Meal Planner

Create a web application for searching recipes and planning weekly meals.

**Domain:** Web Application, Database
**Requirements:** Recipe database with search, dietary filters (vegetarian, gluten-free), ingredient-based search, meal planning calendar, shopping list generation, user accounts, recipe scaling.

---

## Challenge 9: Distributed Key-Value Store

Implement a distributed key-value store with replication and consistency guarantees.

**Domain:** Distributed Systems, Database
**Requirements:** Basic CRUD operations, data replication across nodes, consistency model (eventual or strong), failure detection and recovery, partitioning/sharding, client library, deployment on multiple servers.

---

## Challenge 10: Code Review Dashboard

Build a dashboard that aggregates code review metrics from GitHub repositories.

**Domain:** Web Application, API Integration
**Requirements:** GitHub API integration, metrics (review time, PR size, active reviewers), visualization (charts/graphs), multi-repository support, refresh data periodically, user authentication via GitHub OAuth.

---

## Challenge 11: Network Packet Analyzer

Create a tool that captures and analyzes network traffic in real-time.

**Domain:** Systems Programming, Networking
**Requirements:** Capture packets (using libpcap or similar), parse common protocols (HTTP, DNS, TCP/IP), real-time display, filtering capabilities, save captures to file, statistics and summary views.

---

## Challenge 12: Machine Learning Model Training Pipeline

Build an end-to-end ML pipeline for training image classification models.

**Domain:** Machine Learning, Data Pipeline
**Requirements:** Data ingestion and preprocessing, model architecture definition, training with GPU support, hyperparameter tuning, model evaluation and metrics, model versioning, deployment endpoint, experiment tracking.

---

## Challenge 13: Collaborative Code Editor

Develop a web-based code editor supporting real-time collaborative editing.

**Domain:** Web Application, Real-Time Collaboration
**Requirements:** Syntax highlighting, real-time collaborative editing (multiple cursors), operational transformation or CRDT for conflict resolution, user presence indicators, chat sidebar, save/load files, deploy to hosting platform.

---

## Challenge 14: Smart Home Hub

Create a central hub application for controlling various smart home devices.

**Domain:** IoT, Integration Platform
**Requirements:** Support multiple device protocols (Zigbee, Z-Wave, WiFi), device discovery and pairing, automation rules engine, scheduling, mobile-responsive web UI, REST API, plugin architecture for extensibility.

---

## Challenge 15: Spotify Clone (Basic)

Build a music streaming web application with core Spotify-like features.

**Domain:** Web Application, Media Streaming
**Requirements:** User authentication, upload/stream audio files, playlists, search, basic player controls, user library, responsive design. (Does not need recommendation algorithm or mobile apps).

---

## Challenge 16: Compiler for Simple Language

Implement a compiler for a simple programming language (subset of C or custom language).

**Domain:** Compilers, Language Implementation
**Requirements:** Lexer and parser, abstract syntax tree, semantic analysis (type checking), code generation (to assembly or bytecode), basic optimizations, error reporting with line numbers, standard library (I/O, string functions).

---

## Challenge 17: Container Orchestration System

Build a system for deploying and managing containerized applications across a cluster.

**Domain:** Distributed Systems, DevOps
**Requirements:** Container deployment and scheduling, service discovery, load balancing, health checking and auto-restart, resource limits and allocation, rolling updates, cluster management, CLI and API.

---

## Challenge 18: Social Media Platform

Create a full-featured social media platform similar to Twitter or Instagram.

**Domain:** Web Application, Social Platform
**Requirements:** User profiles and authentication, posts with images/video, follow system, news feed with algorithm, likes and comments, notifications, direct messaging, search, trending topics, mobile apps (iOS and Android), admin moderation tools, CDN for media, scalable infrastructure.

---

## Notes for Assessment

When ranking these challenges, consider:
- **Time to implement:** How long would it take a competent developer?
- **Technical complexity:** How difficult are the core algorithms/systems?
- **Integration complexity:** How many external systems need to work together?
- **Domain knowledge required:** How much specialized knowledge is needed?
- **Testing difficulty:** How hard is it to verify correctness?
- **Deployment complexity:** What does it take to run this in production?
- **AI suitability:** How well could an AI agent assist with this project?

Work with your AI agent to analyze each challenge across these dimensions.
