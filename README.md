# REST APIS

_by [Abhinav NB](https://github.com/ABHINAV112) for NTUOSS TGIFHacks Workshop _

This workshop features a hands on approach to learning the basics of REST APIs. You will learn the types of REST APIs, the components of requests and responses, how to call a REST API and make your very own rest APIs. Familiarity with [JSON](https://www.w3schools.com/whatis/whatis_json.asp), and the [command line interface](https://tutorial.djangogirls.org/en/intro_to_command_line/) will aid you in this workshop.

## Introduction

API stands for Application Programming Interface. An API is a software intermediary that allows two applications to talk to each other. In other words, an API is the messenger that delivers your **request** to the provider that you’re requesting it from and then delivers the **response** back to you. Click [here](https://www.youtube.com/watch?v=s7wmiS2mSXY&t=1s), to see a nice video explaining APIs.

### [Types of APIs](https://ffeathers.wordpress.com/2014/02/16/api-types/)

APIs are classified broadly based on the types of interactions they allow to make. For instance if you want to interact with hardware, you could use a hardware API. These are some of the major classifications:

- Web Service APIs
- WebSocket APIs
- Library based APIs
- Class-based APIs
- OS functions and routines
- Object remoting APIs
- Hardware APIs

---

## Web Service APIs

A type of API which provides access to its service via a **URL**. Requests are made to a server, the server then processes the information in the request and sends back a response.

### Different types

- SOAP
- XML-RPC and JSON-RPC
- REST (becoming more used in modern times, easy to use)

---

## Types of REST APIs

Conventionally, REST APIs fall under into 4 different types of categories. These categories are important during the implementation of an API as they are a component of the request. An API maybe classified based on the following information, however sometimes an API of a certain type may not perform the function stated below. For example, a POST API maybe used to retrieve data from a server. The following are very loose definitions needed to establish a convention for making APIs. Their implementation is completely dependent on the creator. For the rest of the content, API and REST API shall be used interchangeably.

### GET

This type of API which is used to retrieve information of a record from the server, the main data to be processed is recieved from parameters and the URL.

### POST

This type of API which is used to create a new record in the server, the data to be processed is sent primarily through a body of data in the request.

### PUT

This type of API which is used to update existing values of a record in the server, the data to be processed is sent through a mixture of parameters and body.

### DELETE

This type of API which is used to delete a record from a server, the data to be processed is sent through a mixture of parameters and body.

## Components of REST API requests(JSON)

This section describes the format of data which should be sent to the server while making an API call(reqest structure). We are covering only JSON requests in this workshop, the following are the key-value attributes which will be sent to the server.

### Url

The http/https address referring to the API hosted on the web(can also be done through a local host).

```javascript
  "url": "https://bestjeanist.sandbox.arcadier.io/api/v2/users/",
```

### Parameters

The URL may contain some additional information which can be used by the server.

```javascript
  "url": "https://bestjeanist.sandbox.arcadier.io/api/v2/users/key=128'"
```

The parameter here is key.

### Method

Indicates the type of API being used, whether it is GET, POST, PUT or DELETE.

```javascript
  "method": "POST"
```

### Headers

Stores important meta data, describing the data of the response being sent to the server. The server reads this data and decides in what manner the rest of the data is to be processed.

```javascript
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer 78bb6ee7-38df-4940-b2cf-1bfa12cbbade",
    "cache-control": "no-cache"
  },
```

There are several header tags which can be used, click [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) to find out more about them.

### Data/Body

This is the body of data sent to the server inside the request, this data will be processed by the server and a response will be sent back.
<br>
NOTE: json can be stringified while sending to the server, it can also be sent raw

```javascript
  "data": "{\n  \"ItemDetail\": {\n    \"ID\": \"00000000-0000-0000-0000-000000000000\"\n  },\n  \"Quantity\": 0,\n  \"Notes\": \"string\",\n  \"CartItemType\": \"string\"\n}"
```

## Components of REST API responses

This section describes the format of data which is recieved after making an API call, the response has 2 important components.

### Status

The status is a number sent by the server. This number describes whether the API call was succesful or not, if the API call was not succesful it tells you what error went on.

Some common codes you may run into are

```
200 - success
400 - bad request
401 - unauthorized
403 - forbidden
404 - error not found
500 - internal server error
```

Click [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) for a list of all the codes.

### Body

The body contains the information processed by the server, this is the information you will use to perform your computation and manipulations. The structure of the body is completely dependent on the creator of the API, his documentation will tell you more about the

---

## Client Side interaction

[Postman](https://www.postman.com/) is a very useful tool which can be used for making calls to APIs. There will be a demo in showing how to use postman.

## Server side code

In this work shop we will be using python and the flask library to make server side code.
