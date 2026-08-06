from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
	@abstractmethod
	def pay(self, amount: float) -> None:
		pass


class CreditCardPayment(PaymentStrategy):
	def pay(self, amount: float) -> None:
		print(f"Paid {amount:.2f} using Credit Card")


class PayPalPayment(PaymentStrategy):
	def pay(self, amount: float) -> None:
		print(f"Paid {amount:.2f} using PayPal")


class BitcoinPayment(PaymentStrategy):
	def pay(self, amount: float) -> None:
		print(f"Paid {amount:.2f} using Bitcoin")


class PaymentProcessor:
	def __init__(self, strategy: PaymentStrategy) -> None:
		self.strategy = strategy

	def set_strategy(self, strategy: PaymentStrategy) -> None:
		self.strategy = strategy

	def process_payment(self, amount: float) -> None:
		self.strategy.pay(amount)


if __name__ == "__main__":
	processor = PaymentProcessor(CreditCardPayment())
	processor.process_payment(100.0)

	processor.set_strategy(PayPalPayment())
	processor.process_payment(250.0)

	processor.set_strategy(BitcoinPayment())
	processor.process_payment(500.0)
