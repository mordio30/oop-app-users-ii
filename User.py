class User:
    # Class variable to store all user posts
    User_posts = []

    def __init__(self, name, email, drivers_license):
        """Initialize a new user with their personal information and an empty list of posts."""
        self.Name = name
        self.Email = email
        self.Drivers_license = drivers_license
        self.posts = []  # Stores posts from this specific user

    def create_a_post(self):
        """Allows a user to create a post with a title and body."""
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        post = {"title": title, "content": content, "author": self.Name}
        
        self.posts.append(post)   # Add to user's personal posts
        User.User_posts.append(post)  # Add to global user posts list

        print("Post created successfully!")

    def delete_a_post(self):
        """Allows a user to delete one of their posts by index."""
        if not self.posts:
            print("You have no posts to delete.")
            return

        # Display all posts for reference
        print("Your posts:")
        for i, post in enumerate(self.posts, 1):
            print(f"{i}. {post['title']}")

        try:
            post_index = int(input("Enter the post number to delete: ")) - 1
            if 0 <= post_index < len(self.posts):
                removed_post = self.posts.pop(post_index)  # Remove from user posts
                User.User_posts.remove(removed_post)  # Remove from global posts
                print("Post deleted successfully!")
            else:
                print("Invalid post number.")
        except ValueError:
            print("Please enter a valid number.")

    def see_my_posts(self):
        """Displays all posts from the current user."""
        if not self.posts:
            print("You have no posts.")
        else:
            print(f"Posts by {self.Name}:")
            for post in self.posts:
                print(f"Title: {post['title']}\nContent: {post['content']}\n")

    @classmethod
    def see_all_posts(cls):
        """Displays all posts from all users."""
        if not cls.User_posts:
            print("No posts available.")
        else:
            print("All User Posts:")
            for post in cls.User_posts:
                print(f"Author: {post['author']}\nTitle: {post['title']}\nContent: {post['content']}\n")


# Example Usage (You can manually call these functions to test)
if __name__ == "__main__":
    user1 = User("John", "john@email.com", "FDUI87")
    user2 = User("Mike", "mike@email.com", "AB12345")
    user3 = User("Zack", "zack@email.com", "XY67890")

    # Manually call these for testing
    user1.create_a_post()
    user2.create_a_post()
    user3.create_a_post()

    user1.see_my_posts()
    User.see_all_posts()

    user1.delete_a_post()
    user1.see_my_posts()
    User.see_all_posts()
