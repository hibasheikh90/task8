# Tasks: Simple Calculator

**Input**: Design documents from `/specs/simple-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: The tests are included as requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

-   **[P]**: Can run in parallel (different files, no dependencies)
-   **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
-   Include exact file paths in descriptions

## Path Conventions

-   **Single project**: `src/`, `tests/` at repository root
-   Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

-   [ ] T001 Create `calculator_app.py` for Streamlit UI.
-   [ ] T002 Create `operations.py` for core arithmetic logic.
-   [ ] T003 Create `test_operations.py` for unit tests.

---

## Phase 2: User Story 1 - Perform Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Implement core arithmetic operations and display results in Streamlit.

**Independent Test**: Can be fully tested by opening the Streamlit application, entering numbers, selecting an operation, and verifying the displayed result.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

-   [ ] T004 [P] [US1] Unit test for `add` function in `test_operations.py`.
    -   Test Case: `add(5, 3)` should return `8`.
    -   Test Case: `add(-1, 1)` should return `0`.
-   [ ] T005 [P] [US1] Unit test for `subtract` function in `test_operations.py`.
    -   Test Case: `subtract(5, 3)` should return `2`.
    -   Test Case: `subtract(3, 5)` should return `-2`.
-   [ ] T006 [P] [US1] Unit test for `multiply` function in `test_operations.py`.
    -   Test Case: `multiply(5, 3)` should return `15`.
    -   Test Case: `multiply(5, 0)` should return `0`.
-   [ ] T007 [P] [US1] Unit test for `divide` function (positive cases) in `test_operations.py`.
    -   Test Case: `divide(6, 3)` should return `2.0`.
    -   Test Case: `divide(5, 2)` should return `2.5`.

### Implementation for User Story 1

-   [ ] T008 [P] [US1] Implement `add` function in `operations.py`.
-   [ ] T009 [P] [US1] Implement `subtract` function in `operations.py`.
-   [ ] T010 [P] [US1] Implement `multiply` function in `operations.py`.
-   [ ] T011 [P] [US1] Implement `divide` function (initial version) in `operations.py`.
-   [ ] T012 [P] [US1] Implement Streamlit UI: input fields for `number1` and `number2` in `calculator_app.py`.
-   [ ] T013 [P] [US1] Implement Streamlit UI: radio buttons for selecting operation in `calculator_app.py`.
-   [ ] T014 [US1] Implement Streamlit UI: display calculated `result` in `calculator_app.py`.
-   [ ] T015 [US1] Integrate `operations.py` functions with `calculator_app.py` UI logic.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently (excluding division by zero error handling).

---

## Phase 3: User Story 2 - Handle Division by Zero (Priority: P1)

**Goal**: Implement safe division by zero handling and display an error.

**Independent Test**: Can be fully tested by opening the Streamlit application, entering a non-zero number, entering "0" into the second number field, selecting "Divide", and verifying the displayed error message.

### Tests for User Story 2 ⚠️

-   [ ] T016 [P] [US2] Unit test for `divide` function (division by zero) in `test_operations.py`.
    -   Test Case: `divide(5, 0)` should raise a `ValueError` or return a specific error string.

### Implementation for User Story 2

-   [ ] T017 [US2] Enhance `divide` function in `operations.py` to raise an error or return an error message for division by zero.
-   [ ] T018 [US2] Update Streamlit UI in `calculator_app.py` to catch division by zero errors and display "Error: Cannot divide by zero".

**Checkpoint**: All user stories should now be independently functional, including division by zero error handling.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final verification

-   [ ] T019 Run all unit tests using `pytest`.
-   [ ] T020 Manually verify Streamlit UI functionality for all operations, including valid inputs and division by zero error handling.

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately
-   **User Stories (Phase 2+)**: All depend on Setup phase completion
    -   User Story 1 and User Story 2 can proceed in parallel for their distinct functionalities, but US2 refines the `divide` function from US1.
-   **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

-   **User Story 1 (P1)**: Can start after Setup (Phase 1) - No dependencies on other stories for initial implementation.
-   **User Story 2 (P1)**: Can start after Setup (Phase 1) - Depends on the initial `divide` function from US1, but primarily enhances it.

### Within Each User Story

-   Tests MUST be written and FAIL before implementation
-   Core implementation before UI integration
-   Story complete before moving to next priority (though US1 and US2 can have overlapping development due to `divide` function refinement)

### Parallel Opportunities

-   All Setup tasks can run in parallel.
-   Unit tests for different operations can be developed in parallel.
-   UI input fields and operation selection can be developed in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Focus)

1.  Complete Phase 1: Setup.
2.  Complete Phase 2: User Story 1 (initial arithmetic functions and basic UI).
3.  **STOP and VALIDATE**: Test User Story 1 independently (excluding division by zero for now).

### Incremental Delivery (Adding Division by Zero Handling)

1.  After MVP, proceed to Phase 3: User Story 2 (division by zero handling).
2.  Test User Story 2 independently.
3.  Finally, proceed to Phase 4: Polish & Cross-Cutting Concerns (run all tests, final UI verification).
