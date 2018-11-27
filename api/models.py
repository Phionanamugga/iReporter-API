class Record:
    # this class defines the record created by a user
    def __init__(self, record_id, createdOn, created_by, record_type, title,
                 description, location, status, images, videos, comments):
        self.record_id = record_id
        self.createdOn = createdOn
        self.created_by = created_by
        self.record_type = record_type
        self.title = title
        self.description = description
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos
        self.comments = comments

    def get_record(self):
        return {
            "record_id": self.record_id,
            "created_on": self.createdOn,
            "created_by": self.created_by,
            "record_type": self.record_type,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
            "comments": self.comments
        }


class User:
    # this class defines the details of a user
    def __init__(self, user_id, firstname, lastname, othernames, email,
                 phonenumber, username, registered_on):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self. othernames = othernames
        self. email = email
        self.phonenumber = phonenumber
        self.username = username
        self. registered_on = registered_on

    def get_user_details(self):
        # this function gets user details
        return {
            "user_id": self.user_id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            " othernames": self.othernames,
            "email": self.email,
            "phonenumber": self.phonenumber,
            "username": self.username,
            "registered_on": self.registered_on,
        }
