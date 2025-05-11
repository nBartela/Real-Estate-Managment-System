# Real-Estate-Managment-System
FROM CLASS:
# Overview
The goal of this project is to build a real estate management application. Users can register with the application, add their payment information and personal details, and most importantly, search and book properties.

# Data Requirements
User
For each User, we should record their name, one or more addresses, and email address. Users can be either agents or prospective renters and are identified by their email address.
For agents, we should also record their job title, the real estate agency they work for, and their contact information.
For prospective renters, we should record their rental preferences (e.g., desired move-in date, preferred location, and budget) as well as their credit card information. A prospective renter can have multiple credit cards, and for each credit card, we associate it with a payment address (one of the User's addresses). Additionally, we record the User's preferred location.
Property Information
The database should record information about Users, properties, prices, and bookings.

Property: 
The main asset of the real estate agency is properties.
A property has a unique identifier, a type (e.g., apartment, house), a location, and a description. For each property, record the city it is located in (e.g., Chicago) and the state (if applicable).
For the project, we will consider the following types of properties:
Houses: Houses have a location, number of rooms, and square footage.
Apartments: Apartments have a location, number of rooms, square footage, and building type.
Commercial Buildings: Commercial buildings have a location, square footage, and type of business.
For each property, we need to store information such as the address, price, and availability.
Price: Each property has a rental price.
Booking: A property booking is for a particular Renter. For each booking, we store which of the Renter's credit cards was used to make the booking.
BONUS: Additional Property Types
Extend the schema to include information about the neighborhood, such as crime rates and nearby schools.
BONUS: Neighborhood Information
Store information about additional property types, such as vacation homes and land.
BONUS: Reward Program
Renters can join a reward program. If a Renter is registered in the reward program, we store a reward point count for the Renter. For every property booking, the Renter receives reward points equal to the rental price of the property.

# Application Requirements
The application should support the following actions. We indicate for each action whether it can be executed by agents or prospective renters.

A user can create an account by registering with an email address (prospective renters and agents).
Add/modify payment/address information: A user holding an account can register/modify/delete credit cards and addresses for their account (prospective renters).
Add/Delete/Modify properties (agents only).
Search for properties (prospective renters and agents).
Book properties (prospective renters only).
Registration
The application should allow both agents and prospective renters to register.

# Payment Information and Addresses
Renters can add/modify/delete addresses and payment methods (credit cards). Addresses that are payment addresses (billing) for a credit card cannot be deleted before deleting the credit card.

# Search for Properties
The application should allow a user to search for properties. The minimal information provided should be a location and a date for the property. The user can select whether they want to search for a rental or a sale property. Additionally, the user can provide a limit for the number of bedrooms, the price range, and the property type (e.g., apartment, house, etc.).

Only properties that are located in the specified location and available on the date provided by the user should be shown. Furthermore, the properties must fulfill all the additional requirements stated by the user. For each property, show the price, number of bedrooms, property type, and property description.

The user can specify how results should be ordered: by price or by number of bedrooms.

# Booking Properties
The application should allow a user to book a property. For each booking, the User should be able to view the details of the property, the rental period (start and end date), the payment method used, and the total cost of the rental.

The Renter should be able to choose the rental period (start and end date) and the payment method. A Renter holding an account can make a booking using one of their saved payment methods. For each booking, the Renter should be able to view the total cost of the rental, the rental period, and the payment method.

# Manage Bookings
Renters can browse the bookings they have made, view the details of each booking, and cancel bookings if necessary. If a booking is canceled, the rental cost will be refunded to the Renter's saved payment method, if applicable.

Agents, on the other hand, can view all bookings made for properties under their agency, including the details of the Renter, the property, the rental period, and the payment method used. Agents can also cancel bookings made for their properties, with the rental cost refunded to the Renter's saved payment method.
