# Testing for The Wee Norn Irish Box

## Contents

- [Code Validation](#code-validation)
- [User Stories](#user-stories)
- [Branches](#branches)
- [Responsiveness](#responsiveness)
- [Performance](#performance)
- [Manual Testing](#manual-testing)
- [Known Bugs](#known-bugs)
- [Other Issues](#other-issues)

---

## Code Validation

[W3C Markup Validator](https://validator.w3.org/)

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

[JS Hint](https://jshint.com/)

[PEP8 Online](http://pep8online.com/)

[Contents](#contents)

---

## User Stories

### First Time Visitor

### Registered User

[Contents](#contents)

---

## Branches

[Contents](#contents)

---

## Responsiveness

[Responsively](https://responsively.app/)

[Contents](#contents)

---

## Performance

[Lighthouse](https://developers.google.com/web/tools/lighthouse)

[Contents](#contents)

---

## Manual Testing

[Contents](#contents)

---

## Known Bugs

Box App Toasts:

- Currently, subscribers box contents are limited to two products from each product category
- If a subscriber exceeds this limit for a category by trying to add a product from that specific category, both a success and an error toast will display
- The success toast will inform the subscriber that they've successfully added that item to their box even though that item isn't added to their box
- The error toast works as it should, informing the user that they've reached their limit for that specific category

[Contents](#contents)

---

## Other Issues

Stripe Subscription:

- The original idea for this project was to create a subscription service that would allow subscribers to receive their snack box each month
- While trying to implement a stripe subscription plan, I was unable to generate any successful payments
- Due to work commitments/project submission deadline impending, I opted for my back-up plan of a one time payment option, keeping the same price of £10 per box

[Contents](#contents)

---
