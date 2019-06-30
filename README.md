# WeatherWizard

WeatherWizard is a full stack application that allows users to subscribe to a mailing list and be sent discounts based on the weather in their area.

## Running the Project
### Front-end

The front-end application is built with JavaScript & React.

After cloning, run the following commands
```bash
cd frontend
yarn start
```
- Users can navigate to localhost:3000 to signup!
### Backend

The backend application is built with Python & Django with a MySQL database.

After cloning, run the following commands
```bash
cd backend
python manage.py runserver 8080
```
- Emails can now be sent to users with the following command:
```bash
 python manage.py sendemails
```

## Choices and Challenges
- This was my first time building a project with *Django*
- This was my first time building a project from scratch with *React*

I chose these technologies because I wanted to learn something new, and I definitely did! I have past experience with building Java webservers that use static html.

### Project Specifications
[Klaviyo](http://klaviyo.com/weather-app)