## General Concept

A reasoning system based on concepts, attributes, relationships, and actions. Instead of complex 2D/3D systems, it uses the simplest possible architecture for a proof-of-concept.

## System Architecture

### 1. Text Parser

* **Input:** text ("Alice is in the house. An apple is in the park")
* **Function:** extract concepts and relationships
* **Output:** concepts + relationships (only explicitly defined attributes)

### 2. World Model

* **Input:** concepts + relationships from the parser
* **Function:** assign an X coordinate to each concept
* **Output:** state graph with spatial attributes

### 3. Relationship Analyzer

* **Input:** snapshot of the world model
* **Function:** calculate current relationships ("what is next to what")
* **Output:** current relationships

### 4. Action Executor

* **Input:** snapshot + action parameters (only movement for now)
* **Function:** change the state
* **Output:** new snapshot

### 5. Goal System (future)

* Goal setting → search for a sequence of actions
* Causal analysis
* Planning of complex scenarios

## Examples of Operation

* Initial: "Alice is in the house" → Alice.x = 10, house.x = 10
* Action: "move(Alice, park)" → Alice.x = 50
* Analysis: "Alice is in the park" (coordinates match)

## MVP Limitations

* 5 fixed concepts
* Only X coordinate
* Single action (movement)
* No learning yet

**Pros:** Simplicity, modularity, easy to test
