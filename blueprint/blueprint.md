FORMAT: 1A
HOST: https://api.pathwar.net

# Pathwar API
An autonomous pathwar API for the [Pathwar](http://www.pathwar.net/) Ecosystem

## Authentication
To be defined.

## Media Types
Where applicable this API uses the [HAL+JSON](https://github.com/mikekelly/hal_specification/blob/master/hal_specification.md) media-type to represent resources states and affordances.

Requests with a message-body are using plain JSON to set or update resource states.

## Error States
The common [HTTP Response Status Codes](https://github.com/for-GET/know-your-http-well/blob/master/status-codes.md) are used.









# Group Sessions

## Session [/sessions/{session_id}]

This resource represents one particular session identified by its *session_id*.

The Session resource has the following attributes:

- name
- created_at
- active

+ Parameters

    + session_id (string) ... ID of the Session in the form of a hash

+ Model (application/hal+json)

    JSON representation of a Session Resource.

    + Body

            {
              "session_id": "41",
              "created_at": "2014-04-14T02:15:15Z",
              "active": true
            }

### Retrieve a Session [GET]

Retrieve a Session by its *session_id*.

+ Response 200

    [Session][]

### Edit a Session [PUT]

To update a Session, send a JSON with updated value for one or more of the Session resource attributes. All attributes values (states) from the previous version of this Session are carried over by default if not included in the hash.

+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }

+ Response 200
    [Session][]

### Delete a Session [DELETE]

Delete a Session. **warning** This action **permanently** removes the session from the database.

+ Response 204

## Sessions Collection [/sessions]

Collection of all Sessions.

The Sessions Collection resource has the following attributes:

- total

In addition it **embeds** *Session Resources* in the Pathwar Sessions API

+ Model (application/hal+json)

    HAL+JSON representation of Sessions Collection Resource. The Sessions resources in collections are embedded. Note the embedded Sessions resource are incomplete representations of the Session in question. Use the respective Session link to retrieve its full representation.

    + Headers

            Link: </sessions>;rel="self",</sessions?page=2>;rel="next"

    + Body

            {
                "_links": {
                    "self": { "href": "/sessions" },
                    "next": { "href": "/sessions?page=2" }
                },
                "_embedded": {
                    "sessions": [
                        {
                            "_links" : {
                                "self": { "href": "/sessions/41" }
                            },
                            "id": "41",
                            "created_at": "2014-04-14T02:15:15Z",
                            "active": true
                        }
                    ]
                },
                "total": 1
            }

### List all Sessions [GET]

+ Response 200

    [Sessions Collection][]

### Create a Session [POST]
To create a new Session simply provide a JSON hash of the *description* and *content* attributes for the new Session.

+ Request (application/json)

        {
          "description": "Description of Session",
          "content": "String content"
        }

+ Response 201

    [Session][]












# Group Users

## User [/users/{user_id}]
This resource represents one particular user identified by its *user_id*.

The User resource has the following attributes:
- user_id
- created_at

+ Parameters
    + user_id (string) ... ID of the User in the form of a hash

+ Model (application/hal+json)
    JSON representation of a User Resource.
    + Headers

            Link: </users/42>;rel="self",<users>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/users/42" },
                "parent": { "href": "/users" },
              },
              "user_id": "42",
              "created_at": "2014-04-14T02:15:15Z"
            }

### Retrieve a User [GET]
Retrieve a User by its *user_id*.
+ Response 200
    [User][]

### Edit a User [PUT]
To update a User, send a JSON with updated value for one or more of the User resource attributes.
All attributes values (states) from the previous version of this User are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [User][]

### Delete a User [DELETE]
Delete a User. **warning** This action **permanently** removes the User from the database.
+ Response 204


## Users Collection [/users]
Collection of all Users.

The Users Collection resource has the following attributes:
- total

In addition it **embeds** *User Resources* in the Pathwar Users API

+ Model (application/hal+json)
    HAL+JSON representation of Users Collection Resource.
    The User resources in collections are embedded.
    Note the embedded User resource are incomplete representations of the User in question.
    Use the respective User link to retrieve its full representation.
    + Headers

            Link: </users>;rel="self",</users?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/users" },
                    "next": { "href": "/users?page=2" }
                },
                "_embedded": {
                    "users": [
                        {
                            "_links" : {
                                "self": { "href": "/users/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }

### List all Users [GET]
+ Response 200
    [Users Collection][]

### Create a User [POST]
To create a new User simply provide a JSON hash of the *description* and *content* attributes for the new User.
+ Request (application/json)

        {
          "description": "Description of User",
          "content": "String content"
        }

+ Response 201
    [User][]














# Group Achievements

## Achievement [/achievements/{achievement_id}]
This resource represents one particular achievement identified by its *achievement_id*.

The Achievement resource has the following attributes:
- achievement_id
- created_at

+ Parameters
    + achievement_id (string) ... ID of the Achievement in the form of a hash

+ Model (application/hal+json)
    JSON representation of a Achievement Resource.
    + Headers

            Link: </achievements/42>;rel="self",<achievements>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/achievements/42" },
                "parent": { "href": "/achievements" },
              },
              "achievement_id": "42",
              "created_at": "2014-04-14T02:15:15Z"
            }

### Retrieve a Achievement [GET]
Retrieve a Achievement by its *achievement_id*.
+ Response 200
    [Achievement][]

### Edit a Achievement [PUT]
To update a Achievement, send a JSON with updated value for one or more of the Achievement resource attributes.
All attributes values (states) from the previous version of this Achievement are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [Achievement][]

### Delete a Achievement [DELETE]
Delete a Achievement. **warning** This action **permanently** removes the Achievement from the database.
+ Response 204


## Achievements Collection [/achievements]
Collection of all Achievements.

The Achievements Collection resource has the following attributes:
- total

In addition it **embeds** *Achievement Resources* in the Pathwar Achievements API

+ Model (application/hal+json)
    HAL+JSON representation of Achievements Collection Resource.
    The Achievement resources in collections are embedded.
    Note the embedded Achievement resource are incomplete representations of the Achievement in question.
    Use the respective Achievement link to retrieve its full representation.
    + Headers

            Link: </achievements>;rel="self",</achievements?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/achievements" },
                    "next": { "href": "/achievements?page=2" }
                },
                "_embedded": {
                    "achievements": [
                        {
                            "_links" : {
                                "self": { "href": "/achievements/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }

### List all Achievements [GET]
+ Response 200
    [Achievements Collection][]

### Create a Achievement [POST]
To create a new Achievement simply provide a JSON hash of the *description* and *content* attributes for the new Achievement.
+ Request (application/json)

        {
          "description": "Description of Achievement",
          "content": "String content"
        }

+ Response 201
    [Achievement][]







# Group Groups

## Group [/groups/{group_id}]
This resource represents one particular group identified by its *group_id*.

The Group resource has the following attributes:
- group_id
- created_at

+ Parameters
    + group_id (string) ... ID of the Group in the form of a hash

+ Model (application/hal+json)
    JSON representation of a Group Resource.
    + Headers

            Link: </groups/42>;rel="self",<groups>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/groups/42" },
                "parent": { "href": "/groups" },
              },
              "group_id": "42",
              "created_at": "2014-04-14T02:15:15Z"
            }

### Retrieve a Group [GET]
Retrieve a Group by its *group_id*.
+ Response 200
    [Group][]

### Edit a Group [PUT]
To update a Group, send a JSON with updated value for one or more of the Group resource attributes.
All attributes values (states) from the previous version of this Group are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [Group][]

### Delete a Group [DELETE]
Delete a Group. **warning** This action **permanently** removes the Group from the database.
+ Response 204


## Groups Collection [/groups]
Collection of all Groups.

The Groups Collection resource has the following attributes:
- total

In addition it **embeds** *Group Resources* in the Pathwar Groups API

+ Model (application/hal+json)
    HAL+JSON representation of Groups Collection Resource.
    The Group resources in collections are embedded.
    Note the embedded Group resource are incomplete representations of the Group in question.
    Use the respective Group link to retrieve its full representation.
    + Headers

            Link: </groups>;rel="self",</groups?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/groups" },
                    "next": { "href": "/groups?page=2" }
                },
                "_embedded": {
                    "groups": [
                        {
                            "_links" : {
                                "self": { "href": "/groups/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }

### List all Groups [GET]
+ Response 200
    [Groups Collection][]

### Create a Group [POST]
To create a new Group simply provide a JSON hash of the *description* and *content* attributes for the new Group.
+ Request (application/json)

        {
          "description": "Description of Group",
          "content": "String content"
        }

+ Response 201
    [Group][]





















# Group Levels

## Level [/levels/{level_id}]
This resource represents one particular level identified by its *level_id*.

The Level resource has the following attributes:
- level_id
- created_at

+ Parameters

    + level_id (string) ... ID of the Level in the form of a hash

+ Model (application/hal+json)
    JSON representation of a Level Resource.
    + Headers

            Link: </levels/42>;rel="self",<levels>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/levels/42" },
                "parent": { "href": "/levels" },
              },
              "level_id": "42",
              "created_at": "2014-04-14T02:15:15Z"
            }

### Retrieve a Level [GET]
Retrieve a Level by its *level_id*.
+ Response 200
    [Level][]

### Edit a Level [PUT]
To update a Level, send a JSON with updated value for one or more of the Level resource attributes.
All attributes values (states) from the previous version of this Level are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [Level][]

### Delete a Level [DELETE]
Delete a Level. **warning** This action **permanently** removes the Level from the database.
+ Response 204


## Levels Collection [/levels]
Collection of all Levels.

The Levels Collection resource has the following attributes:
- total

In addition it **embeds** *Level Resources* in the Pathwar Levels API

+ Model (application/hal+json)
    HAL+JSON representation of Levels Collection Resource.
    The Level resources in collections are embedded.
    Note the embedded Level resource are incomplete representations of the Level in question.
    Use the respective Level link to retrieve its full representation.
    + Headers

            Link: </levels>;rel="self",</levels?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/levels" },
                    "next": { "href": "/levels?page=2" }
                },
                "_embedded": {
                    "levels": [
                        {
                            "_links" : {
                                "self": { "href": "/levels/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }

### List all Levels [GET]
+ Response 200
    [Levels Collection][]

### Create a Level [POST]
To create a new Level simply provide a JSON hash of the *description* and *content* attributes for the new Level.
+ Request (application/json)

        {
          "description": "Description of Level",
          "content": "String content"
        }

+ Response 201
    [Level][]


















# Group Logs

## Log [/logs/{log_id}]
This resource represents one particular log identified by its *log_id*.

The Log resource has the following attributes:
- log_id
- created_at

+ Parameters

    + log_id (string) ... ID of the Log in the form of a hash

+ Model (application/hal+json)
    JSON representation of a Log Resource.
    + Headers

            Link: </logs/42>;rel="self",<logs>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/logs/42" },
                "parent": { "href": "/logs" },
              },
              "log_id": "42",
              "created_at": "2014-04-14T02:15:15Z"
            }

### Retrieve a Log [GET]
Retrieve a Log by its *log_id*.
+ Response 200
    [Log][]

### Edit a Log [PUT]
To update a Log, send a JSON with updated value for one or more of the Log resource attributes.
All attributes values (states) from the previous version of this Log are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [Log][]

### Delete a Log [DELETE]
Delete a Log. **warning** This action **permanently** removes the Log from the database.
+ Response 204


## Logs Collection [/logs]
Collection of all Logs.

The Logs Collection resource has the following attributes:
- total

In addition it **embeds** *Log Resources* in the Pathwar Logs API

+ Model (application/hal+json)
    HAL+JSON representation of Logs Collection Resource.
    The Log resources in collections are embedded.
    Note the embedded Log resource are incomplete representations of the Log in question.
    Use the respective Log link to retrieve its full representation.
    + Headers

            Link: </logs>;rel="self",</logs?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/logs" },
                    "next": { "href": "/logs?page=2" }
                },
                "_embedded": {
                    "logs": [
                        {
                            "_links" : {
                                "self": { "href": "/logs/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }

### List all Logs [GET]
+ Response 200
    [Logs Collection][]

### Create a Log [POST]
To create a new Log simply provide a JSON hash of the *description* and *content* attributes for the new Log.
+ Request (application/json)

        {
          "description": "Description of Log",
          "content": "String content"
        }

+ Response 201
    [Log][]











# Group Level Validations

## Level Validation [/level_validations/{level_validation_id}]
This resource represents one particular level validation identified by its *level_validation_id*.

The Level Validation resource has the following attributes:
- level_validation_id
- created_at

+ Parameters
    + level_validation_id (string) ... ID of the Level Validation in the form of a hash

+ Model (application/hal+json)
    JSON representation of a Level Validation Resource.
    + Headers

            Link: </level_validations/42>;rel="self",<level validations>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/level_validations/42" },
                "parent": { "href": "/level_validations" },
              },
              "level_validation_id": "42",
              "level_id": "43",
              "group_id": "44",
              "author_id": "45",
              "comment": "",
              "created_at": "2014-04-14T02:15:15Z"
              "approvation_status": ""
            }

### Retrieve a Level Validation [GET]
Retrieve a Level Validation by its *level_validation_id*.
+ Response 200
    [Level Validation][]

### Edit a Level Validation [PUT]
To update a Level Validation, send a JSON with updated value for one or more of the Level Validation resource attributes.
All attributes values (states) from the previous version of this Level Validation are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [Level Validation][]

### Delete a Level Validation [DELETE]
Delete a Level Validation. **warning** This action **permanently** removes the Level Validation from the database.
+ Response 204


## Level Validations Collection [/level_validations]
Collection of all Level Validations.

The Level Validations Collection resource has the following attributes:
- total

In addition it **embeds** *Level Validation Resources* in the Pathwar Level Validations API

+ Model (application/hal+json)
    HAL+JSON representation of Level Validations Collection Resource.
    The Level Validation resources in collections are embedded.
    Note the embedded Level Validation resource are incomplete representations of the Level Validation in question.
    Use the respective Level Validation link to retrieve its full representation.
    + Headers

            Link: </level_validations>;rel="self",</level_validations?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/level_validations" },
                    "next": { "href": "/level_validations?page=2" }
                },
                "_embedded": {
                    "level validations": [
                        {
                            "_links" : {
                                "self": { "href": "/level_validations/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }


### List all Level Validations [GET]
+ Response 200
    [Level Validations Collection][]

### Create a Level Validation [POST]
To create a new Level Validation simply provide a JSON hash of the *description* and *content* attributes for the new Level Validation.
+ Request (application/json)

        {
          "description": "Description of Level Validation",
          "content": "String content"
        }

+ Response 201
    [Level Validation][]









# Group Level Purchases

## Level Purchase [/level_purchases/{level_purchase_id}]
This resource represents one particular level purchase identified by its *level_purchase_id*.

The Level Purchase resource has the following attributes:
- level_purchase_id
- created_at

+ Parameters
    + level_purchase_id (string) ... ID of the Level Purchase in the form of a hash

+ Model (application/hal+json)
    JSON representation of a Level Purchase Resource.
    + Headers

            Link: </level_purchases/42>;rel="self",<level purchases>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/level_purchases/42" },
                "parent": { "href": "/level_purchases" },
              },
              "level_purchase_id": "42",
              "level_id": "43",
              "group_id": "44",
              "author_id": "45",
              "comment": "",
              "created_at": "2014-04-14T02:15:15Z"
              "approvation_status": ""
            }

### Retrieve a Level Purchase [GET]
Retrieve a Level Purchase by its *level_purchase_id*.
+ Response 200
    [Level Purchase][]

### Edit a Level Purchase [PUT]
To update a Level Purchase, send a JSON with updated value for one or more of the Level Purchase resource attributes.
All attributes values (states) from the previous version of this Level Purchase are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [Level Purchase][]

### Delete a Level Purchase [DELETE]
Delete a Level Purchase. **warning** This action **permanently** removes the Level Purchase from the database.
+ Response 204


## Level Purchases Collection [/level_purchases]
Collection of all Level Purchases.

The Level Purchases Collection resource has the following attributes:
- total

In addition it **embeds** *Level Purchase Resources* in the Pathwar Level Purchases API

+ Model (application/hal+json)
    HAL+JSON representation of Level Purchases Collection Resource.
    The Level Purchase resources in collections are embedded.
    Note the embedded Level Purchase resource are incomplete representations of the Level Purchase in question.
    Use the respective Level Purchase link to retrieve its full representation.
    + Headers

            Link: </level_purchases>;rel="self",</level_purchases?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/level_purchases" },
                    "next": { "href": "/level_purchases?page=2" }
                },
                "_embedded": {
                    "level purchases": [
                        {
                            "_links" : {
                                "self": { "href": "/level_purchases/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }


### List all Level Purchases [GET]
+ Response 200
    [Level Purchases Collection][]

### Create a Level Purchase [POST]
To create a new Level Purchase simply provide a JSON hash of the *description* and *content* attributes for the new Level Purchase.
+ Request (application/json)

        {
          "description": "Description of Level Purchase",
          "content": "String content"
        }

+ Response 201
    [Level Purchase][]












# Group Level Steps

## Level Step [/level_steps/{level_step_id}]
This resource represents one particular level step identified by its *level_step_id*.

The Level Step resource has the following attributes:
- level_step_id
- created_at

+ Parameters
    + level_step_id (string) ... ID of the Level Step in the form of a hash

+ Model (application/hal+json)
    JSON representation of a Level Step Resource.
    + Headers

            Link: </level_steps/42>;rel="self",<level steps>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/level_steps/42" },
                "parent": { "href": "/level_steps" },
              },
              "level_step_id": "42",
              "level_id": "43",
              "group_id": "44",
              "author_id": "45",
              "comment": "",
              "created_at": "2014-04-14T02:15:15Z"
              "approvation_status": ""
            }

### Retrieve a Level Step [GET]
Retrieve a Level Step by its *level_step_id*.
+ Response 200
    [Level Step][]

### Edit a Level Step [PUT]
To update a Level Step, send a JSON with updated value for one or more of the Level Step resource attributes.
All attributes values (states) from the previous version of this Level Step are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [Level Step][]

### Delete a Level Step [DELETE]
Delete a Level Step. **warning** This action **permanently** removes the Level Step from the database.
+ Response 204


## Level Steps Collection [/level_steps]
Collection of all Level Steps.

The Level Steps Collection resource has the following attributes:
- total

In addition it **embeds** *Level Step Resources* in the Pathwar Level Steps API

+ Model (application/hal+json)
    HAL+JSON representation of Level Steps Collection Resource.
    The Level Step resources in collections are embedded.
    Note the embedded Level Step resource are incomplete representations of the Level Step in question.
    Use the respective Level Step link to retrieve its full representation.
    + Headers

            Link: </level_steps>;rel="self",</level_steps?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/level_steps" },
                    "next": { "href": "/level_steps?page=2" }
                },
                "_embedded": {
                    "level steps": [
                        {
                            "_links" : {
                                "self": { "href": "/level_steps/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }


### List all Level Steps [GET]
+ Response 200
    [Level Steps Collection][]

### Create a Level Step [POST]
To create a new Level Step simply provide a JSON hash of the *description* and *content* attributes for the new Level Step.
+ Request (application/json)

        {
          "description": "Description of Level Step",
          "content": "String content"
        }

+ Response 201
    [Level Step][]

















# Group Group Successs

## Group Success [/group_successs/{group_success_id}]
This resource represents one particular group success identified by its *group_success_id*.

The Group Success resource has the following attributes:
- group_success_id
- created_at

+ Parameters
    + group_success_id (string) ... ID of the Group Success in the form of a hash

+ Model (application/hal+json)
    JSON representation of a Group Success Resource.
    + Headers

            Link: </group_successs/42>;rel="self",<group successs>;rel="parent"
    + Body

            {
              "_links": {
                "self": { "href": "/group_successs/42" },
                "parent": { "href": "/group_successs" },
              },
              "group_success_id": "42",
              "group_id": "43",
              "group_id": "44",
              "author_id": "45",
              "comment": "",
              "created_at": "2014-04-14T02:15:15Z"
              "approvation_status": ""
            }

### Retrieve a Group Success [GET]
Retrieve a Group Success by its *group_success_id*.
+ Response 200
    [Group Success][]

### Edit a Group Success [PUT]
To update a Group Success, send a JSON with updated value for one or more of the Group Success resource attributes.
All attributes values (states) from the previous version of this Group Success are carried over by default if not included in the hash.
+ Request (application/json)

        {
          "description": "new description",
          "value": 42
        }
+ Response 200
    [Group Success][]

### Delete a Group Success [DELETE]
Delete a Group Success. **warning** This action **permanently** removes the Group Success from the database.
+ Response 204


## Group Successs Collection [/group_successs]
Collection of all Group Successs.

The Group Successs Collection resource has the following attributes:
- total

In addition it **embeds** *Group Success Resources* in the Pathwar Group Successs API

+ Model (application/hal+json)
    HAL+JSON representation of Group Successs Collection Resource.
    The Group Success resources in collections are embedded.
    Note the embedded Group Success resource are incomplete representations of the Group Success in question.
    Use the respective Group Success link to retrieve its full representation.
    + Headers

            Link: </group_successs>;rel="self",</group_successs?page=2>;rel="next"
    + Body

            {
                "_links": {
                    "self": { "href": "/group_successs" },
                    "next": { "href": "/group_successs?page=2" }
                },
                "_embedded": {
                    "group successs": [
                        {
                            "_links" : {
                                "self": { "href": "/group_successs/42" }
                            },
                            "id": "42",
                            "created_at": "2014-04-14T02:15:15Z",
                        }
                    ]
                },
                "total": 1
            }


### List all Group Successs [GET]
+ Response 200
    [Group Successs Collection][]

### Create a Group Success [POST]
To create a new Group Success simply provide a JSON hash of the *description* and *content* attributes for the new Group Success.
+ Request (application/json)

        {
          "description": "Description of Group Success",
          "content": "String content"
        }

+ Response 201
    [Group Success][]
