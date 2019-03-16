# Dunbell: A dumbbell for your Dunbar's number
Dunbell's number is a claim that the average human can only keep track of a
limited number of social relationships - somewhere in the order of 150.

Most of us will have met far more interesting and valuable people than this
number: folks you meet travelling, friends of friends, cool distant relations.
Social media platforms are designed for superficial widely broadcast posts, not
meaningful one-on-one interactions. Dunbell aims to help fill this gap:

- Remember the name of your old primary school friend's mum
- Keep track of who it was that gave you great advise about permaculture that
  one time
- Discover acquaintances with similar interests who you could put in touch


## TODOs
- Security for login
- Ability to search for friend by name/nicname
- Ability to add a friend through interface
- Ability to add fact
- Ability to search by fact
- Ability to bump fact up in importance
- Default importances for fact types
- Show friendship graph with edge types
  - friendship
  - family
  - relationship
- Friends have categories, e.g. "Festivals", "EA"
- Integrations with emails/Telegram etc?

## Implemented
- Page shows friend facts
- More important/useful facts rise to the top
- Facts can have categories associated with them, E.g.
  - family
  - hobbies
  - study

## Infrastructure
- Hosted on AWS
- Data saved in CSVs in S3 and accessed with S3 Select
- Eventually, serverless

## Table schemas
Friend
- id
  - 42
- full_name
  - "Alex Vance"
- display_name
  - "Alex"
- DoB
  - March 1989

Names
- ref_name
  - "Alex Vance"
- alt_name
  - "Lexy"

Facts
- id
  - 42
- fact_type
  - "Family"
- [fact_subtype]
  - "Sister"
- fact_name
  - "Jolene"
- [fact_ref]
  - 72
- fact_deets
  - "Younger sister. Good relationship"
- [fact_importance]
  - [0, 5]
