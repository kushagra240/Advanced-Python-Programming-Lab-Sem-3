from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
	@abstractmethod
	def pay(self, amount: float) -> None:
		pass


class CreditCardPayment(PaymentStrategy):
	def pay(self, amount: float) -> None:
		print(f"Paid {amount:.2f} using Credit Card")
