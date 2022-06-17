from flask import json, jsonify, request
import requests
import requests_cache

#importing and creating cache method to cache API calls to save on memory & improve performance
requests_cache.install_cache(cache_name='hatchways_cache', backend='sqlite', expire_after=180)


class Blogs():

    def __init__(self, tags, sortby = '', dir = ''):
        self.tags = tags
        self.sortby = sortby
        self.dir = dir 
        self.tag_list = []
        self.blog_list = []

    def check_tags(self):
        for post in self.blog_list:
                for tag in post['tags']:
                    self.tag_list.append(tag)

        self.tag_list = set(self.tag_list)
        return self.tag_list

    def check_sortby(self):
        fields = {'id', 'reads', 'likes', 'popularity'}
        if self.sortby not in fields:
            return False
        return True

    def check_dir(self):
        if self.dir != 'asc' and self.dir != 'desc':
            return False
        return True

    def fetch_posts(self):
        # Calling upon the API for an individual tag
        if len(self.tags) == 1:
            r = requests.get(f"https://api.hatchways.io/assessment/blog/posts?tag={self.tags[0]}")
            if r.status_code == 200:
                data = r.json()
                  
            if r.status_code == 400:
                return False

    
            for post in data['posts']:
                self.blog_list.append(post)
                        
        # Calling upon the API for every user inputed tag individually 
        else:
            for tag in self.tags: 
                r = requests.get(f"https://api.hatchways.io/assessment/blog/posts?tag={tag}")
                if r.status_code == 200:
                    data = r.json()
                        
                if r.status_code == 400:
                    return False

                # Using the unique Post ID # to look for membership within a list of ALL Post Ids.
                # If the Unique ID is already in the list we do not add it to the final blog list.
                
                for post in data['posts']:
                    self.blog_list.append(post)
                        
    
    def sort_posts(self, posts):
        sorted_list = []
        sortby_list = []

        if self.sortby == '' and self.dir == '':
            return posts

        #creating a list of sortby values that we can sort in either asc or desc 
        # order to sort final blog list
        for post in posts:
            sortby_list.append(post[self.sortby])
            sorted_list.append('')

        if self.dir == 'asc':
            sortby_list.sort()
        elif self.dir == 'desc':
            sortby_list.sort(reverse=True)

        #creating final sorted list based on sortby & dir value 
        for post in posts:
            sorted_list[sortby_list.index(post[self.sortby])] = post
            sortby_list[sortby_list.index(post[self.sortby])] = 'x' #accounts for duplicate sortby values
        
        return sorted_list

    def remove_dups(self, posts):
        post_ids = []
        non_dups_list = []
        for post in posts:
            if post['id'] not in post_ids:
                non_dups_list.append(post)
                post_ids.append(post['id'])

        return non_dups_list

    def get_posts(self):
        unique_posts = self.remove_dups(self.blog_list)
        sorted_posts = self.sort_posts(unique_posts)
        return jsonify(sorted_posts), 200

    
