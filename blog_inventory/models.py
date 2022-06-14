import requests


class Blogs():
    
    def __init__(self, tags, sortby, dir):
        self.tags = tags
        self.sortby = sortby 
        self.dir = dir
        self.blog_list = self.fetch_posts(tags)

    def fetch_posts(self, tags):

        post_ids = []
        blog_list =[]

        # Calling upon the API for an individual tag
        if len(tags) == 1:
            r = requests.get(f"https://api.hatchways.io/assessment/blog/posts?tag={tags[0]}")
            if r.status_code == 200:
                data = r.json()
                
                
            if r.status_code == 400:
                return "error: Tags parameter is required"

            for post in data['posts']:
                blog_list.append(post)
                        
        # Calling upon the API for every user inputed tag individually 
        else:
            for tag in tags: 
                r = requests.get(f"https://api.hatchways.io/assessment/blog/posts?tag={tag}")
                if r.status_code == 200:
                    data = r.json()
                    
                    
                if r.status_code == 400:
                    return "error: Tags parameter is required"

                # Using the unique Post ID # to look for membership within a list of ALL Post Ids.
                # If the Unique ID is already in the list we do not add it to the final blog list.
                
                for post in data['posts']:
                    if post['id'] not in post_ids:
                        blog_list.append(post)
                        post_ids.append(post['id'])

        self.blog_list = blog_list
        self.sort_posts()


    def sort_posts(self):

        sorted_list = []
        sortby_list = []

        if self.sortby == '' and self.dir == '':
            self.sorted_blog_list = self.blog_list

        #creating a list of sortby values that we can sort in either asc or desc 
        # order to assist in sorting final blog list
    
        for post in self.blog_list:
            sortby_list.append(post[self.sortby])
            sorted_list.append('')

        if self.dir == 'asc':
            sortby_list.sort()
        elif self.dir == 'desc':
            sortby_list.sort(reverse=True)

        for post in self.blog_list:
            sorted_list[sortby_list.index(post[self.sortby])] = post
            sortby_list[sortby_list.index(post[self.sortby])] = 'x' #accounts for duplicate sortby values

               
        self.sorted_blog_list = sorted_list
        print('this is sorted blog list')
        print(self.sorted_blog_list)

    def aslist(self):
        return self.sorted_blog_list

    def __iter__(self):
        return iter(self.aslist())

    
