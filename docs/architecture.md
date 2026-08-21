                         ┌──────────────────┐
                         │     STUDENT      │
                         └────────┬─────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │       FRONTEND         │
                     │    React + TypeScript  │
                     └────────────┬───────────┘
                                  │
                              REST API
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │        BACKEND         │
                     │        FastAPI         │
                     └───────┬────────┬───────┘
                             │        │
                ┌────────────┘        └─────────────┐
                ▼                                   ▼
      ┌──────────────────┐                 ┌──────────────────┐
      │    PostgreSQL    │                 │ Adaptive Engine  │
      │     Database     │                 │     Python       │
      └──────────────────┘                 └────────┬─────────┘
                                                     │
                                          ┌──────────┴─────────┐
                                          │                    │
                                          ▼                    ▼
                                   Mastery Model       Recommendation
                                                        Engine


Eventually4
                              ┌──────────────────┐
                              │   AI / LLM Layer │
                              └────────┬─────────┘
                                       │
                         ┌─────────────┴─────────────┐
                         ▼                           ▼
                  Question Generation         Explanation Generation


                 STUDENT
                    │
                    ▼
               ATTEMPT DATA
                    │
                    ▼
              ┌─────────────┐
              │   MASTERY   │
              │             │
              │ Linear  .82 │
              │ Trees   .61 │
              │ NN      .43 │
              └──────┬──────┘
                     │
                     ▼
              RECOMMENDATION
                  ENGINE
                     │
             ┌───────┴────────┐
             ▼                ▼
        Which concept?    What difficulty?
             │                │
             └───────┬────────┘
                     ▼
                  QUESTION
                     │
                     ▼
                  STUDENT


┌──────────────────────────────┐
│       STUDENT MODEL          │
│                              │
│ Concept → P(Mastered)        │
└──────────────┬───────────────┘
               │
               ▼
       ┌───────────────┐
       │ Recommendation│
       │    Engine     │
       └───────┬───────┘
               │
       ┌───────┴────────┐
       ▼                ▼
   Concept           Difficulty
       │                │
       └───────┬────────┘
               ▼
            Question
               │
               ▼
            Student
               │
               ▼
             Answer
               │
               ▼
        Bayesian Update
               │
               ▼
       New P(Mastered)
               │
               └───────────────→ repeat