from examples.structured_output.ticket_system import TicketCategory, process_ticket


def billing_issue_example() -> None:
    ticket = process_ticket(customer_message="Hi there, I have a question about my bill. Can you help me?")

    assert ticket.category == TicketCategory.BILLING

    print(ticket.reply)
    print(ticket.category)
    print(ticket.confidence)
    print(ticket.sentiment)


def order_issue_example() -> None:
    ticket = process_ticket(customer_message="I would like to place an order.")
    assert ticket.category == TicketCategory.ORDER


def main() -> None:
    billing_issue_example()
    order_issue_example()
    print()


if __name__ == "__main__":
    main()
