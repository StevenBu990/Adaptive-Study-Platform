# Adaptive Learning Model

## Mastery Score

For each student-concept pair, the system maintains a
`mastery_score` between 0 and 1.

The mastery score represents the estimated probability
that the student has mastered the concept.

Examples:

0.10 → Very unlikely to have mastered the concept
0.30 → Likely still struggling
0.50 → Uncertain
0.70 → Probably understands the concept
0.90 → Very likely to have mastered the concept