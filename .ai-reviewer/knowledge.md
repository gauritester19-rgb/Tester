# Tester reviewer notes

## Architecture

This is a small FastAPI student-management API implemented entirely in `main.py`. It uses Pydantic for request validation and a module-level Python list as its in-memory data store. Endpoints cover health/status, listing, searching, filtering, counting, and CRUD operations for students.

## Conventions

- Define request payloads with Pydantic `BaseModel`; `Student` in `main.py` enforces `name` and `course` minimum lengths and restricts `age` to `1–100`.
- Student records are dictionary-shaped objects containing `id`, `name`, `age`, and `course`; preserve this response shape across CRUD endpoints (`main.py`).
- Collection responses are wrapped in a `"students"` key, including `/students`, `/students/search`, and `/students/course/{course_name}`.
- Successful mutations return a human-readable `"message"` plus the affected `"student"` (`create_student`, `update_student`, and `delete_student` in `main.py`).
- Missing IDs consistently raise `HTTPException(status_code=404, detail="Student not found")`.
- Name search is case-insensitive substring matching, while course filtering is case-insensitive exact matching (`search_student` and `get_students_by_course`).
- Endpoint functions use straightforward synchronous `def` handlers and operate directly on the shared `students` list.
- IDs are generated as one greater than the current maximum, with `0` as the empty-list default (`create_student`).

## Intentional non-standard choices

- There is no database, repository layer, or persistence: `students` is deliberately an in-memory module-level list in `main.py`; data resets when the process restarts.
- Responses use plain dictionaries rather than response models, and the API does not declare explicit response schemas.
- Delete mutates the list while iterating, then immediately returns; this is intentional because the first matching ID is removed and iteration stops.

## Watch out for

- Do not silently change the established response envelopes or 404 detail text; clients may depend on them.
- Preserve case-insensitive behavior for name and course lookups.
- Avoid introducing duplicate route behavior or changing route paths; `/students/{student_id}` must continue to coexist with `/students/search`, `/students/count`, and `/students/course/{course_name}`.
- Be cautious with ID generation: `max(...) + 1` is only suitable for this in-memory, single-process implementation and is not safe as a persistent or concurrent storage strategy.
- Mutating the global list is process-local and not concurrency-safe; flag changes that assume shared persistence across workers or restarts.
