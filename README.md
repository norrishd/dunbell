# Friend Tracker

## Functions
- Security for login
- Ability to search for friend by name/nicname
- Page shows friend facts
- More important/useful facts rise to the top
- Facts can have categories associated with them, E.g.
  - family
  - hobbies
  - study
- Ability to add a friend through interface
- Show friendship graph with edge types
  - friendship
  - family
  - relationship
- Friends have categories, e.g. "Festivals", "EA"
- Integrations with emails/Telegram etc?

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
