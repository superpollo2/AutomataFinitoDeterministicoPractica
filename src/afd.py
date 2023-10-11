
ESTADOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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

        self.STATES = iter(ESTADOS)
        try:
            self.symbols.remove('e') #lamda
        except:
            pass

        # Inicialización de contrucción AF
        self.ParseTree(self.tree)
        self.CalcFollowPos()

    def CalcFollowPos(self):
        for node in self.nodes:
            if node.value == '*':
                for i in node.lastpos:
                    child_node = next(filter(lambda x: x._id == i, self.nodes))
                    child_node.followpos += node.firstpos
            elif node.value == '.':
                for i in node.c1.lastpos:
                    child_node = next(filter(lambda x: x._id == i, self.nodes))
                    child_node.followpos += node.c2.firstpos

        # Inicia la generación de estados
        initial_state = self.nodes[-1].firstpos

        # nodos que tienen simbolos
        self.nodes = list(filter(lambda x: x._id, self.nodes))
        self.augmented_state = self.nodes[-1]._id

        # Usamos recursión para leer toda la expresión 
        self.CalcNewStates(initial_state, next(self.STATES))

    def CalcNewStates(self, state, curr_state):

        if not self.states:
            self.states.append(set(state))
            if self.augmented_state in state:
                self.accepting_states.update(curr_state)

        # Iteramos por cada símbolo
        for symbol in self.symbols:

            # Obtener los nodos con el mismo simbolo
            same_symbols = list(
                filter(lambda x: x.value == symbol and x._id in state, self.nodes))

            # Crear un nuevo estado con los nodos
            new_state = set()
            for node in same_symbols:
                new_state.update(node.followpos)

            # El nuevo estado no esta en la lista
            if new_state not in self.states and new_state:

                # letra del nuevo estado
                self.states.append(new_state)
                next_state = next(self.STATES)

                # agregar estado a la función de transición
                try:
                    self.trans_func[next_state]
                except:
                    self.trans_func[next_state] = dict()

                try:
                    existing_states = self.trans_func[curr_state]
                except:
                    self.trans_func[curr_state] = dict()
                    existing_states = self.trans_func[curr_state]

                # Add the reference
                existing_states[symbol] = next_state
                self.trans_func[curr_state] = existing_states

                # es un accepting_state?
                if self.augmented_state in new_state:
                    self.accepting_states.update(next_state)

                # Repetir con el nuevo estado
                self.CalcNewStates(new_state, next_state)

            elif new_state:
                # si el estado ya existe, cual de ellos es
                for i in range(0, len(self.states)):

                    if self.states[i] == new_state:
                        state_ref = ESTADOS[i]
                        break

                # agregar simbolo de transición 
                try:
                    existing_states = self.trans_func[curr_state]
                except:
                    self.trans_func[curr_state] = {}
                    existing_states = self.trans_func[curr_state]

                existing_states[symbol] = state_ref
                self.trans_func[curr_state] = existing_states

    def ParseTree(self, node):
        method_name = node.__class__.__name__ + 'Node'
        method = getattr(self, method_name)
        return method(node)

    def LetterNode(self, node):
        new_node = Node(self.iter, [self.iter], [
                        self.iter], value=node.value, nullable=False)
        self.nodes.append(new_node)
        return new_node

    def OrNode(self, node):
        node_a = self.ParseTree(node.a)
        self.iter += 1
        node_b = self.ParseTree(node.b)

        is_nullable = node_a.nullable or node_b.nullable
        firstpos = node_a.firstpos + node_b.firstpos
        lastpos = node_a.lastpos + node_b.lastpos

        self.nodes.append(Node(None, firstpos, lastpos,
                               is_nullable, '|', node_a, node_b))
        return Node(None, firstpos, lastpos, is_nullable, '|', node_a, node_b)

    def AppendNode(self, node):
        node_a = self.ParseTree(node.a)
        self.iter += 1
        node_b = self.ParseTree(node.b)

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

    def KleeneNode(self, node):
        node_a = self.ParseTree(node.a)
        firstpos = node_a.firstpos
        lastpos = node_a.lastpos
        self.nodes.append(Node(None, firstpos, lastpos, True, '*', node_a))
        return Node(None, firstpos, lastpos, True, '*', node_a)

    def PlusNode(self, node):
        node_a = self.ParseTree(node.a)

        self.iter += 1

        node_b = self.KleeneNode(node)

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

    

    def EvalRegex(self):
        curr_state = 'A'
        for symbol in self.regex:

            if not symbol in self.symbols:
                return 'No'

            try:
                curr_state = self.trans_func[curr_state][symbol]
            except:
                if curr_state in self.accepting_states and symbol in self.trans_func['A']:
                    curr_state = self.trans_func['A'][symbol]
                else:
                    return 'No'

        return 'Yes' if curr_state in self.accepting_states else 'No'

    



