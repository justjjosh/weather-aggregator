# Developer Profile: Josh

## Current Skill Level
- **Python**: Solid foundational knowledge (completed "Full Speed Python" course + extensive practice)
  - Functions, scope, parameters, return statements
  - String operations, list operations, dictionary operations (including nested)
  - OOP: Classes, `__init__`, `self`, inheritance, `super()`, `__str__`, `__iter__`, `__next__`
  - Generators and `yield` keyword
  - Comfortable reading and debugging error messages ("errors are my best friends")
- **FastAPI**: Completed 2 projects with increasing complexity
  - REST API endpoints (GET, POST, PUT, DELETE)
  - Pydantic models for request/response validation
  - Database integration with SQLAlchemy/SQLModel
  - Async endpoints
  - Many-to-many relationships (Notes + Tags project)
- **PostgreSQL**: CRUD operations, relationships (one-to-many, many-to-many), query filtering
- **Docker**: Containerized applications and PostgreSQL in Docker
- **AWS**: Deployed FastAPI apps to AWS (Lambda/ECS/EC2)
- **Git/GitHub**: Foundational version control knowledge

## Learning Goals for This Project
1. Learn to make **external API calls** from FastAPI using `httpx`
2. Understand **async HTTP requests** and `async/await` patterns
3. Learn **caching strategies** to avoid hitting API rate limits
4. Practice **environment variables** with `.env` files for API keys
5. Implement **TTL (Time To Live)** logic for cached data
6. Learn **error handling** for external service failures
7. Understand **graceful degradation** when third-party APIs are down

## Teaching Style (STRICT)
- I am learning. DO NOT generate full code blocks unless I explicitly ask.
- When I ask "How do I do X?", explain the concept with syntax examples, but let ME write the implementation.
- If I paste an error, explain *why* it happened - do not just give me the fix.
- If my code works but is "messy", suggest a refactor and explain *why* it's better.
- Use verbose explanations with references to official documentation when possible.
- Guide me through problems step-by-step rather than solving them for me.
- Exception: If I say "I'm tired, just do it" OR "just show me" - then provide the solution and explain afterward.

## Project Context: Weather API Aggregator

**What this project is:**
A REST API that fetches weather data from an external API (OpenWeatherMap) and caches the results in PostgreSQL to avoid hitting rate limits. Returns cached data if it's less than 10 minutes old.

**Expected features:**
- Accept city name as input
- Fetch current weather from OpenWeatherMap API
- Store the response in PostgreSQL with timestamp
- Return cached data if < 10 minutes old (avoid unnecessary API calls)
- Handle errors gracefully when external API is down
- Use environment variables for API key (don't hardcode secrets!)

**Database schema (1-2 tables):**
1. `weather_cache` - stores city name, weather data (JSON), and timestamp

**Tech stack:**
- FastAPI
- PostgreSQL (in Docker)
- SQLAlchemy or SQLModel for ORM
- `httpx` for async HTTP requests (not `requests` - that's synchronous!)
- `python-dotenv` for environment variables
- Pydantic for schemas
- Docker for containerization
- OpenWeatherMap API (free tier)

**New concepts introduced:**
- Making external API calls from your API
- Async HTTP with `httpx.AsyncClient()`
- Caching to reduce external API load
- TTL (Time To Live) logic
- Environment variables and secrets management
- Error handling for third-party dependencies

## Previous Projects Completed
1. ✅ **Todo API** - Basic CRUD, single table, Docker, AWS deployment
2. ✅ **Notes API with Tags** - Many-to-many relationships, query filtering, timestamps

## Consistency Journey
- Currently on Day 60+ of consistent coding practice
- Posts daily updates on LinkedIn/Twitter
- Committed to becoming a robust Cloud/Software/DevOps Engineer

## Notes for the Agent
- Josh learns best by doing, not by copying
- He values understanding the "why" behind code
- He has autocomplete turned OFF to build muscle memory
- He's not afraid of errors - encourage him to debug
- Celebrate wins - he's come a long way!
- This is his third FastAPI project - he's ready for external API integration
- Focus on explaining async patterns and caching strategies thoroughly