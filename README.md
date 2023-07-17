# Fullstack Affiliates

This repository contains the source code and related files for the Fullstack Affiliates project. Fullstack Affiliates is an affiliate platform that allows users to create, manage, and track affiliate links for marketing campaigns.

## Features

The Fullstack Affiliates platform includes the following features:

- User authentication: Users can create accounts and log in to access the platform.
- Campaign creation: Users can create marketing campaigns and configure details such as name, description, and reward.
- Affiliate link generation: A unique link is generated for each campaign, allowing affiliates to promote it.
- Click and conversion tracking: Clicks on affiliate links are tracked, and conversions are recorded to ensure proper compensation for affiliates.
- Affiliate dashboard: Affiliates have access to a dashboard where they can view statistics, earnings, and manage their campaigns.

## Technologies Used

The Fullstack Affiliates project utilizes the following technologies:

- Frontend:
  - React: JavaScript library for building the user interface.

- Backend:
  - Django: Python web framework for building the backend.
  - PostgreSQL: Relational database management system for storing application data.
  - Docker: Containerization platform for packaging the application and its dependencies.
  - Docker Compose: Tool for defining and running multi-container Docker applications.

## How to Run the Project

Follow the instructions below to run the project on your local machine:

1. Make sure you have Docker and Docker Compose installed on your machine.

2. Clone this repository to your development environment:
   git clone https://github.com/Murilo831/fullstack-afiliados.git
   
3. Navigate to the project directory:
   cd fullstack-afiliados

4. Start the application using Docker Compose:
   docker-compose up

5. Access the application in your browser at `http://localhost:3000`.

The Docker Compose command will automatically build and run the required containers for the Django backend, PostgreSQL database, and React frontend.
