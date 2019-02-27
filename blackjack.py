{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "************************************\n",
      "|    WELCOME TO BLACK JACK GAME    |\n",
      "************************************\n",
      "press c to continue the game or any other key to quit the game:  c\n",
      "Enter your bet amount  :56\n",
      "your balance amount is :44\n",
      "\n",
      "\n",
      "#############\n",
      "PLAYER CARDS:\n",
      "Clover of 6\n",
      "Diamond of j\n",
      "Your point is:16\n",
      "\n",
      "\n",
      "COMPUTER CARDS:\n",
      "Heart of 2\n",
      "##HIDDEN CARD##\n",
      "\n",
      "\n",
      "h for HIT or any other key for STAND:  s\n",
      "#############\n",
      "PLAYER CARDS:\n",
      "Clover of 6\n",
      "Diamond of j\n",
      "Your point is:16\n",
      "\n",
      "\n",
      "COMPUTER CARDS:\n",
      "Heart of 2\n",
      "Spade of 9\n",
      "Spade of 3\n",
      "Spade of 6\n",
      "computer point is:20\n",
      "\n",
      "\n",
      "YOU LOST\n",
      "press c to continue the game or any other key to quit the game:  c\n",
      "Enter your bet amount  :50\n",
      "Insufficient fund!!! enter amount less than 44\n",
      "Enter your bet amount  :43\n",
      "your balance amount is :1\n",
      "\n",
      "\n",
      "#############\n",
      "PLAYER CARDS:\n",
      "Spade of k\n",
      "Clover of 8\n",
      "Your point is:20\n",
      "\n",
      "\n",
      "COMPUTER CARDS:\n",
      "Spade of 2\n",
      "##HIDDEN CARD##\n",
      "\n",
      "\n",
      "h for HIT or any other key for STAND:  h\n",
      "\n",
      "\n",
      "\n",
      "#############\n",
      "PLAYER CARDS:\n",
      "Spade of k\n",
      "Clover of 8\n",
      "Spade of 8\n",
      "Your point is:28\n",
      "\n",
      "\n",
      "COMPUTER CARDS:\n",
      "Spade of 2\n",
      "##HIDDEN CARD##\n",
      "\n",
      "\n",
      "#############\n",
      "PLAYER CARDS:\n",
      "Spade of k\n",
      "Clover of 8\n",
      "Spade of 8\n",
      "Your point is:28\n",
      "\n",
      "\n",
      "COMPUTER CARDS:\n",
      "Spade of 2\n",
      "Clover of k\n",
      "computer point is:14\n",
      "\n",
      "\n",
      "YOU LOST\n",
      "press c to continue the game or any other key to quit the game:  c\n",
      "Enter your bet amount  :1\n",
      "your balance amount is :0\n",
      "\n",
      "\n",
      "#############\n",
      "PLAYER CARDS:\n",
      "Diamond of 3\n",
      "Heart of 7\n",
      "Your point is:10\n",
      "\n",
      "\n",
      "COMPUTER CARDS:\n",
      "Clover of j\n",
      "##HIDDEN CARD##\n",
      "\n",
      "\n",
      "h for HIT or any other key for STAND:  h\n",
      "\n",
      "\n",
      "\n",
      "#############\n",
      "PLAYER CARDS:\n",
      "Diamond of 3\n",
      "Heart of 7\n",
      "Clover of 8\n",
      "Your point is:18\n",
      "\n",
      "\n",
      "COMPUTER CARDS:\n",
      "Clover of j\n",
      "##HIDDEN CARD##\n",
      "\n",
      "\n",
      "h for HIT or any other key for STAND:  s\n",
      "#############\n",
      "PLAYER CARDS:\n",
      "Diamond of 3\n",
      "Heart of 7\n",
      "Clover of 8\n",
      "Your point is:18\n",
      "\n",
      "\n",
      "COMPUTER CARDS:\n",
      "Clover of j\n",
      "Spade of 8\n",
      "computer point is:18\n",
      "\n",
      "\n",
      "IT'S A TIE\n",
      "press c to continue the game or any other key to quit the game:  q\n",
      "Thank you for playing\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "shapes=['Heart','Spade','Diamond','Clover']\n",
    "values=['A','2','3','4','5','6','7','8','9','j','q','k']\n",
    "points={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'j':10,'q':11,'k':12}\n",
    "play=True\n",
    "class Cards():\n",
    "    def __init__(self):\n",
    "        self.my_card=[]\n",
    "        self.actual_card_for_player=[]\n",
    "        self.actual_card_for_computer=[]\n",
    "        self.player_point=0\n",
    "        self.computer_point=0\n",
    "    def total_cards(self):\n",
    "        'This function is to display the entire cards'\n",
    "        for i in shapes:\n",
    "            for j in values:\n",
    "                print(f'{j} of {i} value is {points[j]}')\n",
    "    \n",
    "    #my_card\n",
    "    def create_card(self):\n",
    "        for i in shapes:\n",
    "            for j in values:\n",
    "                self.my_card.append([i,j])\n",
    "    #my_card\n",
    "    \n",
    "    \n",
    "    def show_card(self):\n",
    "        return self.my_card\n",
    "    \n",
    "    def shuffle(self):\n",
    "        random.shuffle(self.my_card)\n",
    "        \n",
    "    def get_card_for_player(self):\n",
    "        self.shuffle()\n",
    "        self.actual_card_for_player.append(self.my_card.pop())\n",
    "        self.player_point=self.calculate_value(self.actual_card_for_player)\n",
    "        \n",
    "    def get_card_for_computer(self):\n",
    "        self.shuffle()\n",
    "        self.actual_card_for_computer.append(self.my_card.pop())\n",
    "        self.computer_point=self.calculate_value(self.actual_card_for_computer)\n",
    "        \n",
    "    def display_player_card(self):\n",
    "        print(\"#############\")\n",
    "        print(\"PLAYER CARDS:\")\n",
    "        for i,j in self.actual_card_for_player:\n",
    "            print(f'{i} of {j}')\n",
    "        print(f'Your point is:{self.player_point}\\n\\n')\n",
    "    \n",
    "    def display_computer_card_with_hidden(self):\n",
    "        print(\"COMPUTER CARDS:\")\n",
    "        print(f'{self.actual_card_for_computer[0][0]} of {self.actual_card_for_computer[0][1]}')\n",
    "        print(f'##HIDDEN CARD##\\n\\n')\n",
    "        \n",
    "    def display_computer_card(self):\n",
    "        print(\"COMPUTER CARDS:\")\n",
    "        for i,j in self.actual_card_for_computer:\n",
    "            print(f'{i} of {j}')\n",
    "        print(f'computer point is:{self.computer_point}\\n\\n')\n",
    "        \n",
    "    def calculate_value(self,cardss):\n",
    "        total_value=0\n",
    "        for i,j in cardss:\n",
    "            total_value=total_value+points[j]\n",
    "        return total_value\n",
    "    \n",
    "    def adjust_computer_cards(self):\n",
    "        while self.computer_point<=23:\n",
    "            self.get_card_for_computer()\n",
    "        if self.computer_point>23:\n",
    "            self.actual_card_for_computer.pop()\n",
    "            self.computer_point=self.calculate_value(self.actual_card_for_computer)\n",
    "    def winorloss(self):\n",
    "        if self.player_point>23:\n",
    "            print(\"YOU LOST\")\n",
    "        elif self.player_point<self.computer_point and  self.computer_point<=23:\n",
    "            print(\"YOU LOST\")\n",
    "        elif self.player_point==self.computer_point:\n",
    "            print(\"IT'S A TIE\")\n",
    "        else:\n",
    "            print(\"YOU WON\")\n",
    "    def clear_cards(self):\n",
    "        self.actual_card_for_player.clear()\n",
    "        self.actual_card_for_computer.clear()\n",
    "class Bank():\n",
    "    def __init__(self):\n",
    "        self.balance=100\n",
    "        self.balance_verify=True\n",
    "    def check_balance(self,bet):\n",
    "        'This function is to check the balance'\n",
    "        if bet<=self.balance:\n",
    "            self.balance=self.balance-bet\n",
    "            self.balance_verify=False\n",
    "        else:\n",
    "            print(f\"Insufficient fund!!! enter amount less than {self.balance}\")\n",
    "    def show_balance(self):\n",
    "        'This function is to return the balance amount'\n",
    "        return self.balance  \n",
    "    def change_balance_verify(self):\n",
    "        self.balance_verify=True\n",
    "    \n",
    "print(\"************************************\")\n",
    "print(\"|    WELCOME TO BLACK JACK GAME    |\")\n",
    "print(\"************************************\")\n",
    "game=Cards()\n",
    "player_bank=Bank()\n",
    "while input(\"press c to continue the game or any other key to quit the game:  \").lower()==\"c\":\n",
    "    while player_bank.balance_verify:\n",
    "        bet=eval(input(\"Enter your bet amount  :\"))\n",
    "        player_bank.check_balance(bet)\n",
    "    player_bank.change_balance_verify()\n",
    "    print(f'your balance amount is :{player_bank.show_balance()}\\n\\n')\n",
    "    game.create_card()\n",
    "    game.get_card_for_player()\n",
    "    game.get_card_for_player()\n",
    "    game.get_card_for_computer()\n",
    "    game.get_card_for_computer()\n",
    "    game.display_player_card()\n",
    "    #game.display_computer_card()\n",
    "    game.display_computer_card_with_hidden()\n",
    "    while input(\"h for HIT or any other key for STAND:  \").lower()==\"h\":\n",
    "        print(\"\\n\\n\")\n",
    "        game.get_card_for_player()\n",
    "        game.display_player_card()\n",
    "        #game.display_computer_card()\n",
    "        game.display_computer_card_with_hidden()\n",
    "        if game.player_point>23:\n",
    "            break\n",
    "    game.adjust_computer_cards()\n",
    "    game.display_player_card()\n",
    "    game.display_computer_card()\n",
    "    game.winorloss()\n",
    "    game.clear_cards()\n",
    "print(\"Thank you for playing\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
