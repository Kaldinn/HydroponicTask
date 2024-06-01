# API Documentation

## Authentication

### Register a new user

- **URL**: `/api/auth/register/`
- **Method**: `POST`
- **Description**: Register a new user.

- **Request Body**:
  ```json
  {
      "username": "your_username",
      "password": "your_password",
      "email": "your_email@example.com"
  }


- **Response**:
  ```json
    {
        "id": 1,
        "username": "your_username",
        "email": "your_email@example.com"
    }

### Obtain JWT token

-**URL**: /api/auth/token/
-**Method**: POST
-**Description**: Obtain a JWT token.
- **Request body**:
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
- **Response**:
    ```json
    {
        "refresh": "your_refresh_token",
        "access": "your_access_token"
    }
### Refresh JWT token

-**URL**: /api/auth/token/refresh/
-**Method**: POST
-**Description**: Refresh an existing JWT token.
- **Request body**:
    ```json
    {
        "refresh": "your_refresh_token"
    }
- **Response**:
    ```json
    {
        "access": "your_new_access_token"
    }


### Hydroponic Systems
### List all hydroponic systems

-**URL**: /api/hydroponic_system/
-**Method**: GET
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Retrieve a list of all hydroponic systems owned by the authenticated user.
- **Response**:
    ```json
    {
        "id": 1,
        "name": "Hydroponic System",
        "description": "Description",
        "owner": 1
    }



### Create a new hydroponic system

-**URL**: /api/hydroponic_system/
-**Method**: POST
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Create a new hydroponic system.
- **Request body**:
  ```json
    {
        "name": "New Hydroponic System",
        "description": "This is a new system."
    }
- **Response**:
    ```json
    {
        "id": 2,
        "name": "New Hydroponic System",
        "description": "This is a new system.",
        "owner": 1
    }


### Retrieve a specific hydroponic system

-**URL**: /api/hydroponic_system/<int:id>/
-**Method**: GET
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Retrieve details of a specific hydroponic system.
- **Response**:
    ```json
    {
        "id": 1,
        "name": "Hydroponic System",
        "description": "Description",
        "owner": 1
    }


### Update a specific hydroponic system

-**URL**: /api/hydroponic_system/<int:id>/
-**Method**: PUT
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Update a specific hydroponic system.
- **Request body**:
  ```json
    {
        "name": "Updated Hydroponic System",
        "description": "Updated description."
    }
- **Response**:
    ```json
    {
        "id": 1,
        "name": "Updated Hydroponic System",
        "description": "Updated description.",
        "owner": 1
    }


### Delete a specific hydroponic system

-**URL**: /api/hydroponic_system/<int:id>/
-**Method**: DELETE
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Delete a specific hydroponic system.
- **Response**:
    ```json
    {
        "detail": "No Content"
    }


### Measurements
### List all measurements

-**URL**: /api/measurement/
-**Method**: GET
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Retrieve a list of all measurements.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "hydroponic_system": 1,
            "timestamp": "2023-05-01T12:34:56Z",
            "ph": 6.5,
            "temperature": 22.0,
            "tds": 300
        },
    ]


### Create a new measurement

-**URL**: /api/measurement/
-**Method**: POST
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Create a new measurement.
- **Request body**:
  ```json
    {
        "hydroponic_system": 1,
        "ph": 6.5,
        "temperature": 22.0,
        "tds": 300
    }
- **Response**:
    ```json
    {
        "id": 2,
        "hydroponic_system": 1,
        "timestamp": "2023-05-01T12:34:56Z",
        "ph": 6.5,
        "temperature": 22.0,
        "tds": 300
    }

### Retrieve a specific measurement

-**URL**: /api/measurement/<int:id>/
-**Method**: GET
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Retrieve details of a specific measurement.
- **Response**:
    ```json
    {
        "id": 1,
        "hydroponic_system": 1,
        "timestamp": "2023-05-01T12:34:56Z",
        "ph": 6.5,
        "temperature": 22.0,
        "tds": 300
    }


### Update a specific measurement

-**URL**: /api/measurement/<int:id>/
-**Method**: PUT
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Update a specific measurement.
- **Request body**:
  ```json
    {
        "ph": 6.8,
        "temperature": 23.0,
        "tds": 310
    }
- **Response**:
    ```json
    {
        "id": 1,
        "hydroponic_system": 1,
        "timestamp": "2023-05-01T12:34:56Z",
        "ph": 6.8,
        "temperature": 23.0,
        "tds": 310
    }


### Delete a specific measurement

-**URL**: /api/measurement/<int:id>/
-**Method**: DELETE
-**Headers**:
-**Authorization**: Bearer your_access_token
-**Description**: Delete a specific measurement.
- **Response**:
    ```json
    {
        "detail": "No Content"
    }
