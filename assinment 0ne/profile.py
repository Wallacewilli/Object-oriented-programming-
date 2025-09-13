# name the  a class called Profile
class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        # These are the attributes of the class
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack  # this should be a list, like ["Python", "Git"]
        self.github_username = github_username
        self.fun_fact = fun_fact

    # Method to introduce yourself
    def introduce(self):
        print("Hi, I’m " + self.name + ". I love " + self.favorite_language + " and my hobby is " + self.hobby + ".")
        print("Fun fact about me: " + self.fun_fact)

    # Method to show your tech stack
    def show_stack(self):
        print(self.name + "'s Tech Stack:")
        for tool in self.tech_stack:
            print("- " + tool)

    # Method to return your GitHub link
    def github_link(self):
        return "https://github.com/Wallacewilli/Object-oriented-programming-/" + self.github_username

# Create your profile
profile = Profile(
    name="Waako Wallace William",
    favorite_language="Python and JavaScript",
    hobby="playing football and swimming",
    tech_stack=["JavaScript", "Node.js"],
    github_username="Wallacewilli",
    fun_fact="I started my own CCTV installation company at the age of 24!"
)

# Call the methods
profile.introduce()
profile.show_stack()
print("GitHub Profile: " + profile.github_link())