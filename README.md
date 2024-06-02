# Datacurve Code Execution Platform

This project is a code execution platform built with Next.js, TypeScript, and Tailwind CSS for the frontend, and FastAPI with SQLite for the backend. Users can write, test, and submit Python 3 code. 

This project is deployed using Vercel - https://datacurve-code-execution-site.vercel.app/. 

## Features

- **Write and Execute Code**: Users can write Python 3 code using a built-in code editor and see the results of their code execution.
- **Persistent Storage**: User code submissions and their outputs are stored in an SQLite database.


## Design Decisions

- Used **Monoco Editor** npm package - powered by VScode and has in-built auto-completion and such other advanced features. 
- **Axios** for secure requests.
- **SQLite** database with **SQLAlchemy**

## Next Steps
- **User Authentication**: Simple token-based authentication to associate code submissions with users.
- **Retrieve Past Submissions**: Users can retrieve and view their past code submissions.
- **Code Formatting**: Add a button to automatically format the user's code.

## Coded By:
Deep Parmar - check out my personal website https://deepparmar02.github.io/