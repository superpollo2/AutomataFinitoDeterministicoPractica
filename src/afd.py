
lETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
from node import Node

class DDFA:
    def __init__(self, tree, symbols, regex):

        #sintaxis del arbol
        self.nodes = list()

        # AF propiedades
        self.symbols = symbols
        self.states = list()
        self.trans_func = dict()
        self.accepting_states = set()
        self.initial_state = 'A'
        
        # propiededes de la clase
        self.tree = tree
        self.regex = regex
        self.augmented_state = None
        self.iter = 1

        self.states = iter(lETTERS)
        try:
            self.symbols.remove('e') #lamda
        except  Exception as e:
            print(f"Ocurrió una excepción: {e}")
        

        # Inicialización de contrucción AF
        self.parse_tree(self.tree)
        self.calc_follow_pos()


    def calc_follow_pos(self):
        try:
            for node in self.nodes:
                if node.value == '*':
                    for i in node.lastpos:
                        child_node = next(filter(lambda x, i=i: x._id == i, self.nodes))
                        child_node.followpos += node.firstpos
                elif node.value == '.':
                    for i in node.c1.lastpos:
                        child_node = next(filter(lambda x, i=i: x._id == i, self.nodes))
                        child_node.followpos += node.c2.firstpos
        except Exception as e:
            
            print(f"Ocurrió una excepción: {e}")
            

        # Inicia la generación de lETTERS
        initial_state = self.nodes[-1].firstpos

        # nodos que tienen simbolos
        self.nodes = list(filter(lambda x: x._id, self.nodes))
        self.augmented_state = self.nodes[-1]._id

        # Usamos recursión para leer toda la expresión 
        self.calc_new_states(initial_state, next(self.states))

    def add_state(self, state):
        if state not in self.states and state:
            self.states.append(state)
            next_state = next(self.states)
            self.trans_func[next_state] = {}
            return next_state
        return None

    def update_transition_function(self, curr_state, symbol, next_state):
        if curr_state not in self.trans_func:
            self.trans_func[curr_state] = {}
        self.trans_func[curr_state][symbol] = next_state

    def update_accepting_states(self, new_state, next_state):
        if self.augmented_state in new_state:
            self.accepting_states.update(next_state)

    def calc_new_states(self, state, curr_state):
        if not self.states:
            self.states.append(set(state))

        if self.augmented_state in state:
            self.accepting_states.update(curr_state)

        for symbol in self.symbols:
            same_symbols = list(filter(lambda x, symbol=symbol: x.value == symbol and x._id in state, self.nodes))
            new_state = set()

            for node in same_symbols:
                new_state.update(node.followpos)

            next_state = self.add_state(new_state)
            if next_state:
                self.update_transition_function(curr_state, symbol, next_state)
                self.update_accepting_states(new_state, next_state)
                self.calc_new_states(new_state, next_state)

    def parse_tree(self, node):
        method_name = node.__class__.__name__ + 'Node'
        method = getattr(self, method_name)
        return method(node)

    def letter_node(self, node):
        new_node = Node(self.iter, [self.iter], [
                        self.iter], value=node.value, nullable=False)
        self.nodes.append(new_node)
        return new_node

    def or_node(self, node):
        node_a = self.parse_tree(node.a)
        self.iter += 1
        node_b = self.parse_tree(node.b)

        is_nullable = node_a.nullable or node_b.nullable
        firstpos = node_a.firstpos + node_b.firstpos
        lastpos = node_a.lastpos + node_b.lastpos

        self.nodes.append(Node(None, firstpos, lastpos,
                               is_nullable, '|', node_a, node_b))
        return Node(None, firstpos, lastpos, is_nullable, '|', node_a, node_b)

    def append_node(self, node):
        node_a = self.parse_tree(node.a)
        self.iter += 1
        node_b = self.parse_tree(node.b)

        is_nullable = node_a.nullable and node_b.nullable
        if node_a.nullable:
            firstpos = node_a.firstpos + node_b.firstpos
        else:
            firstpos = node_a.firstpos

        if node_b.nullable:
            lastpos = node_b.lastpos + node_a.lastpos
        else:
            lastpos = node_b.lastpos

        self.nodes.append(
            Node(None, firstpos, lastpos, is_nullable, '.', node_a, node_b))

        return Node(None, firstpos, lastpos, is_nullable, '.', node_a, node_b)

    def kleene_node(self, node):
        node_a = self.parse_tree(node.a)
        firstpos = node_a.firstpos
        lastpos = node_a.lastpos
        self.nodes.append(Node(None, firstpos, lastpos, True, '*', node_a))
        return Node(None, firstpos, lastpos, True, '*', node_a)

    def plus_node(self, node):
        node_a = self.parse_tree(node.a)

        self.iter += 1

        node_b = self.kleene_node(node)

        is_nullable = node_a.nullable and node_b.nullable
        if node_a.nullable:
            firstpos = node_a.firstpos + node_b.firstpos
        else:
            firstpos = node_a.firstpos

        if node_b.nullable:
            lastpos = node_b.lastpos + node_a.lastpos
        else:
            lastpos = node_b.lastpos

        self.nodes.append(
            Node(None, firstpos, lastpos, is_nullable, '.', node_a, node_b))

        return Node(None, firstpos, lastpos, is_nullable, '.', node_a, node_b)

    

    def eval_regex(self):
        curr_state = 'A'
        for symbol in self.regex:

            if symbol not in self.symbols:
                return 'No'

            try:
                curr_state = self.trans_func[curr_state][symbol]
            except:
                if curr_state in self.accepting_states and symbol in self.trans_func['A']:
                    curr_state = self.trans_func['A'][symbol]
                else:
                    return 'No'

        return 'Yes' if curr_state in self.accepting_states else 'No'

    