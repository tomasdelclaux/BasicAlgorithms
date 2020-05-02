import collections

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, home):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = home

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        if path.endswith("/"):
            path = path[:-1]
        
        for element in path.split("/"):
            current_node = current_node.children[element]
        current_node.handler = handler
        

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        
        if path.endswith("/"):
            path = path[:-1]
        
        for element in path.split("/"):
            if element not in current_node.children:
                return None
            current_node = current_node.children[element]
            
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = collections.defaultdict(RouteTrieNode)



# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, rootHandler, notFound):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie("/")
        self.homepage = rootHandler
        self.notFound = notFound
        

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routes.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/":
            return self.homepage
        isFound = self.routes.find(path)
        if isFound:
            return isFound
        else:
            return self.notFound

    def split_path(self):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        #not needed
        pass



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me", "froggy")
router.add_handler("/home/photos/", "photos")


# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print froggy
print(router.lookup("/home/about/you")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/references"))  # should print not found handler
print(router.lookup("/home/photos"))  # should print photos
print(router.lookup("/home/photos/"))  # should print photos