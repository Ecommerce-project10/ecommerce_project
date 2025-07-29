# E-Commerce Web Application

## Overview
This is a Django-based e-commerce web application designed to facilitate online shopping with features for buyers, sellers, and admins. The application supports user authentication, product browsing, shopping cart functionality, order processing, and admin/seller dashboards, with a responsive design for desktop, tablet, and mobile devices.

## Features
- **User Authentication**: Secure login and signup for buyers, sellers, and admins using Django's Custom User Model.
- **Home Page**: Displays featured products with search functionality and category filters.
- **Product Catalog**: Allows users to browse products with detailed product pages (image, price, description).
- **Shopping Cart**: Buyers can add/remove products and view their cart.
- **Checkout**: Simple form for delivery and payment information.
- **Seller Dashboard**: Sellers can add/edit their products, track orders, and view sales analytics using Chart.js.
- **Admin Panel**: Admins can manage users, products, and orders.
- **Responsive Design**: Built with Bootstrap to ensure compatibility across devices.

## Technology Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL
- **Authentication**: Django Custom User Model
- **Analytics**: Chart.js for sales visualizations

## Project Structure
```
ecommerce_project/
├── accounts/           # User authentication and profile management
├── products/           # Product catalog and details
├── cart/               # Shopping cart functionality
├── orders/             # Order processing and history
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
└── ecommerce/          # Project settings and configuration
```

## User Roles
- **Buyer**:
  - Create account and log in
  - Browse and search products
  - Add products to cart
  - Place orders and view order history
- **Seller**:
  - Create account and log in
  - Add/edit their products
  - Track orders and view sales analytics
- **Admin**:
  - Log in to admin dashboard
  - Manage users (approve sellers, remove users)
  - Edit/delete products
  - View all orders

## Prerequisites
- Python 3.8+
- PostgreSQL
- Django 
- Bootstrap

   ```
## Usage
- **Home Page**: Navigate to `/` to browse featured products and use the search bar.
- **Product Page**: Click on a product to view details and add to cart.
- **Cart**: View and manage cart items at `/cart/`.
- **Checkout**: Proceed to `/checkout/` to enter delivery and payment details.
- **Seller Dashboard**: Sellers can access `/seller/` to manage products and view sales charts.
- **Admin Panel**: Admins can log in at `/admin/` to manage users, products, and orders.


## Team Workflow
- **Team Size**: 6 developers
- **Roles**:
  - 2 Backend Developers: Focus on models, views, and database integration.
  - 2 Frontend Developers: Build templates and integrate Chart.js for analytics.
  - 1 Database Developer: Optimize database schema and queries.
  - 1 Project Manager: Coordinate tasks and ensure integration.
- **Tools**:
  <!-- - **Task Management**: Trello or Jira for task tracking.
  - **Communication**: Slack for daily stand-ups. -->
  - **Version Control**: GitHub for code collaboration.


## License
This project is licensed under the MIT License.