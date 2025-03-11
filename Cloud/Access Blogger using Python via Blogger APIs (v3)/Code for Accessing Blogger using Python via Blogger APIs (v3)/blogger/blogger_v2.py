from __future__ import print_function

import sys

from oauth2client import client
from googleapiclient import sample_tools

# -- my imports --
import os

def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger')

    try:
        users = service.users()

        # Retrieve this user's profile information
        thisuser = users.get(userId='self').execute()

        blogs = service.blogs()

        # Retrieve the list of Blogs this user has write privileges on
        thisusersblogs = blogs.listByUser(userId='self').execute()

        posts = service.posts()

        blog = thisusersblogs['items'][0] # survival8 "For Blogger Account of ashishjain1547@gmail.com"
        blog = thisusersblogs['items'][1] # ashishjain1547 "For Blogger Account of ashishjain1547@gmail.com"

        #print(blog['id'])

        os.chdir('TXT')
        l = os.listdir('.')
        for i in l:
            with open(os.path.join(os.getcwd(), i), mode = 'r') as f:
                fc = f.read()

            if blog['id'] == '1969144627074060944':
                body = {
                        "kind": "blogger#post",
                        "id": blog['id'],
                        "title": i,
                        "content": fc
                        }
                posts.insert(blogId=blog['id'], body=body, isDraft=True).execute()
                #posts.insert(blogId=blog['id'], body='test post', isDraft=True).execute()

    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run'
               'the application to re-authorize')

if __name__ == '__main__':
    main(sys.argv)