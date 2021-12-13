from transitions import Machine



class TG_Chat_Bot(object):
    '''
    Класс состояний бота
    '''
    states = ['rest', 'accept an order', 'payment selection', 'order summary']

    def __init__(self):
        self.type_of_pizza = None
        self.type_of_payment = None
        self.machine = Machine(model=self, states=TG_Chat_Bot.states, initial='rest')
        self.machine.add_transition(trigger='welcome', source='rest', dest='accept an order')
        self.machine.add_transition(trigger='customer reported order', source='accept an order', dest='payment selection')
        self.machine.add_transition(trigger='customer has chosen the form of payment', source='payment selection', dest='order summary')
        self.machine.add_transition(trigger='Summarized the order', source='order summary', dest='rest')
        self.machine.add_transition(trigger='start', source='*', dest='rest')

    def get_type_of_pizza(self, type_of_pizza):
        '''
        меод получения типа пиццы(большой или маленькой)
        '''
        self.type_of_pizza = type_of_pizza
        return self.type_of_pizza


    def get_type_of_payment(self, type_of_payment):
        '''
        Метода получаения типа оплаты заказа("наличка" или "безнал")
        '''
        self.type_of_payment = type_of_payment
        return self.type_of_payment

