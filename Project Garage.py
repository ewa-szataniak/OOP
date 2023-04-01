class ThemeParkGarage:
    def __init__(self):
        self.tickets = list(range(1, 11))
        self.parkingSpaces = list(range(1, 11))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            space = self.parkingSpaces.pop(0)
            self.currentTicket[ticket] = {'paid': False, 'space': space}
            print(f'Please take ticket {ticket} for your parking spot')
            print(f'Available parking spaces: {self.parkingSpaces}')
            return ticket
        else:
            print('Sorry, garage is currently full')
            return None

    def payForParking(self):
        ticket = input('Please enter your parking ticket number: ')
        try:
            ticket = int(ticket)
            if ticket in self.currentTicket and not self.currentTicket[ticket]['paid']:
                payment = input('Please enter payment amount: ')
                if float(payment) < 10:
                    print('Payment received. You have 15 minutes to leave.')
                    self.currentTicket[ticket]['paid'] = True
                else:
                    print('Payment received. Thank you for your generosity!')
                    self.currentTicket[ticket]['paid'] = True
            else:
                print('Invalid ticket number or ticket already paid')
        except ValueError:
            print('Invalid input')

    def leaveGarage(self):
        ticket = input('Please enter your parking ticket number: ')
        try:
            ticket = int(ticket)
            if ticket in self.currentTicket and self.currentTicket[ticket]['paid']:
                space = self.currentTicket[ticket]['space']
                self.parkingSpaces.insert(0, space)
                self.tickets.append(ticket)
                del self.currentTicket[ticket]
                print('Thank you, have a nice day!')
                print(f'Available tickets: {self.tickets}')
                print(f'Available parking spaces: {self.parkingSpaces}')
            elif ticket in self.currentTicket and not self.currentTicket[ticket]['paid']:
                payment = input('Please pay for your parking ticket: ')
                if float(payment) < 10:
                    print('Payment received. Thank you, have a nice day!')
                else:
                    print('Payment received. Thank you for your generosity!')
                self.currentTicket[ticket]['paid'] = True
                space = self.currentTicket[ticket]['space']
                self.parkingSpaces.insert(0, space)
                self.tickets.append(ticket)
                print(f'Available tickets: {self.tickets}')
                print(f'Available parking spaces: {self.parkingSpaces}')
            else:
                print('Invalid ticket number')
        except ValueError:
            print('Invalid input')

    def runGarage(self):
        while True:
            response = input('Welcome to the Theme Park Garage, would you like to park your car? Yes or No? ')
            if response.lower() == 'no':
                print('Okay, have a great day!')
                break
            elif response.lower() == 'yes':
                ticket = self.takeTicket()
                if ticket is not None:
                    while True:
                        response = input('What would you like to do? Pay, Leave, or Back? ')
                        if response.lower() == 'pay':
                            self.payForParking()
                        elif response.lower() == 'leave':
                            self.leaveGarage()
                            break
                        elif response.lower() == 'back':
                            break
                        else:
                            print('Invalid input')

garage = ThemeParkGarage()
garage.runGarage()
