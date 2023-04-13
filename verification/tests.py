"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [5, [(4, 2), (5, 2), (2, 1), (8, 3)]],
            "answer": 13,
        },
        {
            "input": [20, [(5, 9), (4, 10)]],
            "answer": 9,
        },
        {
            "input": [10, [(4, 3), (2, 2), (6, 4), (3, 1)]],
            "answer": 15,
        },
    ],
    "Extra": [
        {
            "input": [15, [(7, 4), (8, 5), (6, 3), (9, 6)]],
            "answer": 24,
        },
        {
            "input": [20, [(10, 5), (15, 8), (7, 4), (12, 6), (4, 2)]],
            "answer": 38,
        },
        {
            "input": [30, [(20, 10), (15, 8), (18, 12), (10, 5), (8, 4), (5, 3)]],
            "answer": 58,
        },
    ]
}
