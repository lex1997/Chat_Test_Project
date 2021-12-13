from transitions import Machine



class TG_Chat_Bot(object):
    '''
    Класс состояний бота
    '''
    states = ['asleep', 'accept an order', 'payment selection', 'order summary']

    def __init__(self):
        self.type_of_pizza = None
        self.type_of_payment = None
        self.machine = Machine(model=self, states=TG_Chat_Bot.states, initial='asleep')
        self.machine.add_transition(trigger='customer_reported_order', source='asleep', dest='accept an order')
        self.machine.add_transition(trigger='customer_has_chosen_the_form_of_payment', source='accept an order', dest='payment selection')
        self.machine.add_transition(trigger='summarized_the_order', source='payment selection', dest='order summary')
        self.machine.add_transition(trigger='stop', source='*', dest='asleep')

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

