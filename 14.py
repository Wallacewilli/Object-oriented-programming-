# my-Profile
class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        # my details of the profile
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack  # this should be a list, like ["Python", "Git"]
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print("Hi, I’m " + self.name + ". I love " + self.favorite_language + " and my hobby is " + self.hobby + ".")
        print("Fun fact about me: " + self.fun_fact)

    # show the tech stack
    def show_stack(self):
        print(self.name + "'s Tech Stack:")
        for tool in self.tech_stack:
            print("- " + tool)

    # putting in the link
    def github_link(self):
        return "https://github.com/Wallacewilli/Object-oriented-programming-.git" + self.github_username

# make a profile of my self 
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