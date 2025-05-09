# 📓 Journal App

This is a full-stack **Journal App** that allows users to create, view, update, and delete journal entries. The app also integrates with an external **journal prompt microservice** (built by a partner) to inspire users with fresh writing prompts.

## 💻 Technologies Used

- Node.js + Express
- HTML/CSS
- JavaScript
- Railway (for API requests to the prompt microservice)

## ✨ Key Features

- 📝 Create journal entries with a title and content
- 🔍 View all saved entries or filter by date
- ✏️ Edit and update existing entries
- ❌ Delete entries with confirmation
- 🤖 Generate a journal prompt using a connected **prompt microservice**
- 🌐 Responsive front-end design

## 🔗 Microservice Integration

The app uses an HTTP request (via Railway) to fetch writing prompts from a journal prompt microservice built by a teammate. Prompts are displayed dynamically on the "New Entry" page to guide and inspire users.

## 🚀 Getting Started

### Prerequisites

- Node.js
- MySQL
- Prompt microservice running and accessible via HTTP

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/villafla/journal_app.git
   cd journal_app
