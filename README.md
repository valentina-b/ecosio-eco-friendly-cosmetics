# ECOSiO - E-Commerce Web App With Eco-Friendly Cosmetics For Men

Code Institute - Final Milestone Project (4) - Full Stack Frameworks With Django

ECOSiO is a multi-page e-commerce web application with a mission to make eco-friendly cosmetics easily available. 
The application focuses on men as target audience and offers a variety of products and content connected to sustainable
lifestyle. The primary purpose of this web app is to provide a trusted marketplace for men interested in sustainability,
environmental issues and personal well-being. ECOSiO's core belief is that both environment and health always come first, 
and we should never be forced to choose one or another. 

As ECOSiO's vision is to revolutionise cosmetic industry from head to toe, the web app is strengthened by having 
features such as blog and loyalty programme. Sustainability can be an overwhelming and, quite often, an expensive choice,
therefore these features support the secondary purpose of the app which is helping customers to stay on the right track and enjoy 
the shopping experience. The idea behind this web app is not to provide a one-time shopping solution but to create a community 
of loyal customers.

Apart from the customer-facing UI, users with admin rights can interact with the web app as well. Although the majority of the
interaction is done through [the Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/), the web app 
provides more pleasant environment for common tasks such as adding, editing and deleting products or blog posts.

**IMPORTANT: This project contains real products from existing brands. Please visit their websites for more information if you
wish to purchase them. Read more about how and why I've used them for this project in the 'Credits' section.**

![App Showcase](readme-files/img-intro.png)

## UX - research and goals

Who are 'green' consumers and why are they so interesting for this project? In [Green Consumerism: An A-to-Z Guide](https://sk.sagepub.com/reference/greenconsumerism/n71.xml)
green consumer has been defined as "_someone who is aware of his or her obligation to protect the environment by selectively purchasing
green products or services. A green consumer tries to maintain a healthy and safe lifestyle without endangering the sustainability of the 
planet and the future of mankind._" According to [GfK](https://digital.gfk.com/understanding-todays-green-consumer), the segment of customers
impacted by the eco-conscious trend has been steadily rising over the past years - from 53% of the overall customers in 2009 to 61% customers 
in 2019. The percentage is particularly high for younger customers, such as Millennials, according to [Global Web Index](https://blog.globalwebindex.com/chart-of-the-week/green-consumerism/).

However, [White, Hardisty and Habib](https://hbr.org/2019/07/the-elusive-green-consumer) write about a fascinating problem when it comes to
green consumers' buying behaviour. It seems that 65% of people say they want to buy purpose-driven brands that advocate sustainability, 
yet only about 26% actually do so. They have been studying how to encourage sustainable consumption for several years, performing their 
own experiments and reviewing research in marketing, economics, and psychology. When it comes to men and sustainability in particular, 
the authors have found out that "some men associate sustainability with femininity, leading them to avoid sustainable options."

What about men and cosmetics? According to [National Retail Federation](https://nrf.com/blog/rise-mens-cosmetics-and-brands-making-their-mark),
men's cosmetics is on the rise as a separate segment of the beauty industry. In the US alone, the revenue forecast for men's skincare products 
is expected [to grow to USD 18.92 billion by 2027.](https://www.grandviewresearch.com/industry-analysis/mens-skincare-products-market) However,
one of the major obstacles when it comes to encouraging men to buy cosmetics is in fact similar to the one mentioned earlier - [Blanchin, Chareyron and Levert](http://www.diva-portal.org/smash/get/diva2:238020/FULLTEXT01.pdf)
write that brands need to fight the widely spread belief that cosmetics is only for women in order to attract male customers.

### Conclusion of the Research

[White, Hardisty and Habib](https://hbr.org/2019/07/the-elusive-green-consumer) give a great example of how Tesla markets its environmentally
friendly cars - "Tesla focuses on the innovative design and functional performance of its cars more than on their green credentials — a message
that resonates with its target market. _This also helps overcome the concern of some men that green products are feminine._" Similarly, 
men's cosmetic industry is fighting that through [design and brand modifications.](https://nrf.com/blog/rise-mens-cosmetics-and-brands-making-their-mark)
It is clear that both of these industries rely heavily on the way the product is presented to the audience, as well as that they need much
stronger prompts and incentives to start the customer buying journey than other e-commerce businesses.

The growing interest in both of these topics indicates a promising potential for business development. On the one hand, sustainability is 
already widely spread as an interest but the users lack encouragement towards paying for such services. On the other hand, men's cosmetics 
as an industry is blooming but it still encounters obstacles, such as associating cosmetics with women.

Since brand identity and incentives seem to be crucial for the user experience (along with the standard features related to e-commerce sites) 
these were my two major focuses throughout the project - how to present well a marketplace for cosmetics to male audience, and how to encourage 
audience interested in sustainability to enter the shopping behaviour.

### Business Goals

As an e-commerce site owner...

* I want the users to be comfortable with the brand identity so that they will want to buy products through my platform.
* I want to offer a shopping journey that is informative and transparent so that the customers develop trust towards the marketplace.
* I want to offer a shopping journey with a higher purpose so that the users prefer my marketplace over other ones.
* I want the customers to be able to actively participate in restoring our eco-system so that they don't feel like their contribution is only passive.
* I want to be able to make changes on the inventory myself so that I don't have to rely on external support when it comes to that.
* I want to have a marketplace offering more than just products so that the customers will have more reasons to come back to the site.
* I want to be able to distinguish loyal customers from one-time buyers so that I can give them better benefits and ensure they will come back to shop more.
* I want to create a community around my brand so that I satisfy customers' need to belong, and they know they're not alone.

### Customer Goals

As a customer...

* I want to buy from a brand I can relate to so that I don't feel uncomfortable or embarrassed throughout the shopping process.
* I want to read more about the company so that I see if the company's values match with mine.
* I want to have information about the products I'm buying easily available so that I’m sure I’m buying exactly what I want and fits my lifestyle.
* I want to be able to filter the products based on my lifestyle so that I can be faster with the buying decision.
* I want to be able to store my shipping details so that it’s easier for me to check out.
* I want to be able to see my orders so that I can track what I buy and spend money on.

As a loyal customer...

* I want to get freebies and rewards for spending money so that I feel like I get a lot more for the money I spend.
* I want an opportunity to get to know the team behind this brand I buy so much from and other like-minded people so that I can see if my loyalty to the brand is a good investment.

## Features and App Sections

Based on the user stories and UX research, I've created an overview of the most important features and information the web app 
should consist of. Since ECOSiO is a multi-page web app, it was very helpful to sketch out the MVP draft and follow it throughout
the project.

In the next few paragraphs I will focus more on the most important sections and features, as well as additional features left to be 
implemented. The next step, described after this chapter, was choosing a database suitable to the project's needs and defining models.

![Features and App Sections Overview](readme-files/img-mvp.png)

### Web App Sections

1. **Navigation at the top** - fixed on the top so that the users are able to navigate themselves anytime. It consists of two HTML code snippets for better responsiveness handling.
1. **Homepage** - introduction to the app and brand identity. The idea is to give a short overview of what ECOSiO is, does and stands for through visual and textual content. Ideally, a user should be able to decide in a few seconds whether they feel connected to the brand identity and be a click away from the shopping feed.
1. **Webshop** - standard e-commerce feed of products with the option to sort products and filter them by category name and product tag. Every product can be added to the cart immediately and links to a product page where the user can read more about it.
1. **Product page** - a page dedicated to individual product. Consists of product description, ingredients and product tags that help with buying decision. At the bottom of the page, there are 3 more products shown to the customer. These 3 products are randomly selected from the same category the main product on the product page belongs to, for example Skincare.
1. **About page** - continues the information shortly provided on the homepage connected to the brand's vision, mission, team and principles regarding product selection for the webshop.
1. **Blog** - a section containing all the blog posts with the focus on sustainability, sustainable lifestyle and synthetic-free cosmetics.
1. **Blog post page** - a page dedicated to individual blog post. It consists of introductory paragraph and at least 2 but up to 3 textual sections. Since the idea is to use this section for showcasing brands ECOSiO is collaborating with as well, majority of the post are written in collaboration with one of the brands the products come from.
1. **Loyalty programme page** - continues the information shortly provided on the homepage connected to the loyalty programme. It describes the process, benefits and reasoning behind creating the programme.
1. **User account** - available to registered/logged in users with the purpose of tracking their loyalty programme status, order history and safely storing shipping details for a smooth checkout.
1. **Admin account** - available to admins and/or users with admin-like rights with the purpose of having access to the orders, user profiles, as well as product and blog inventory. Majority of the information is stored in [the Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/) but the users can also do common tasks such as adding, editing and deleting products or blog posts through ECOSiO's UI.
1. **Footer** - gives users the option to stay up to date with the app via links to social media profiles.

### Features and Django Apps

ECOSiO, [a Django project](https://docs.djangoproject.com/en/3.1/ref/applications/), consists of 8 Django applications listed below. 
As explained in Django's documentation - a Django application describes a Python package that provides some set of features. Applications may be 
reused in various projects.

* `homepage`
* `about`
* `blog`
* `loyalty_programme`
* `products`
* `cart`
* `checkout`
* `profiles`

Some features I've worked on are available across the Django project, while others are tied to a specific Django application. The following list 
of features is structured in a way that should help with understanding how the features are spread throughout the project.

**Navigation**
* always present on the top so that the users are able to navigate themselves anytime. It consists of **the top navigation** (a combination of a brand logo, search box, account related activities and the cart functionality) and **the main navigation** below it (for navigating throughout the main app sections).
* navigation links are compressed into a hamburger menu on mobile and tablet devices so that the main focus of the user is the shopping cart in the top right corner at all times, and not the navigation links.

![Navigation Feature](readme-files/img-features/img-features-navigation.png)

**Search functionality**
* as mentioned in the previous paragraph, a search box is part of the top navigation and is, therefore, accessible on all pages.
* it is collapsed under the hamburger menu on tablet and mobile devices as shown in the image above.
* it allows customers to enter keywords associated with the products they wish to purchase.
* the search results are displayed as a feed of products by using the page templates prepared for the `products` Django app (i.e. webshop).
* the search results show the number of products found for the search query, as well as inform the user if no products were found along with a CTA linked to the webshop's feed.

![Search Feature](readme-files/img-features/img-features-search.png)

**Breadcrumbs**
* breadcrumbs are present throughout the `products` (i.e. webshop), `cart` and `checkout` Django apps and, additionally, throughout the `profiles`.
* the purpose of this feature is to ease the navigation across ECOSiO where navigation links might not be as helpful. Therefore, breadcrumbs don't appear on every webpage.

![Breadcrumbs Checkout Feature](readme-files/img-features/img-features-breadcrumbs-checkout.png)

**Toasts**
* small snippets of messages divided into 4 main categories: `toast_success`, `toast_info`, `toast_warning` and `toast_error`.
* they appear on every page whenever a certain action has been done by the user.
* their purpose is to give feedback on the action a user has just performed, such as logging in, logging out, adding a product to the cart, updating the cart, editing a blog post, finishing the checkout process, adding too many products in the card, donating loyalty points etc.
* it generally consists of the title based on the toast category with a matching text about the action. The `toast_success` toast additionally has cart information, that is hidden on `profiles` pages and for some other activities if nothing is added to the cart.

![Toasts Feature](readme-files/img-features/img-features-toasts.png)

**Django-allauth feature**
* `django-allauth` is a Python package. As writtenin the [django-allauth docs](https://django-allauth.readthedocs.io/en/latest/), it is an "integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication."
* it provides a set of features such as **signup**, **login**, **logout** and **password change**.
* after signing up, a verification email is sent to the registered email to confirm it. Once confirmed, the user can log in with their credentials and access the `profiles` app explained later below.
* the links to these features can be found in the navigation, under the **My Account** dropdown menu, as well as on the pages and throughout the web app (for example, registration prompt window on the `homepage`).

![Django-allauth Feature](readme-files/img-features/img-features-allauth.png)

**Automatic e-mails**
* a gmail account **ecosio.cosmetics@gmail.com** has been created specifically for this project and used as a sender for all verification, reset and confirmation emails.
* for example, users receive an **order confirmation e-mail** after a purchase, **account verification e-mail** after the registration, **password reset email** after requesting a password reset, etc.

![Automatic E-mails Feature](readme-files/img-features/img-features-automatic-emails.png)

**Homepage app**
* `homepage` Django app mainly serving as an introduction to the brand and the marketplace
* the most prominent feature is the **registration prompt** displayed to the visitors that aren't logged in. It's fixed at the bottom of the page and encourages the visitor to create an account by mentioning the 10% discount.
* another two features found on the homepage are the **popular products' gallery**, a feature for the admin team to set 3 products they want to showcase on the page, and the **curated shopping shortcuts** - links to prefiltered product by category. Both of these features mainly aim to be a sneak peek into the webshop.

![Homepage Features](readme-files/img-features/img-features-homepage.png)

**About app**
* `about` Django app is one of the apps that are mostly relying on textual content.
* besides textual content, this app has a set of custom-made icons that summarise what ECOSiO is about and what it offers.

![About Page Features](readme-files/img-features/img-features-about.png)

**Blog app**
* `blog` Django app mostly relies on textual content and can be split into 3 parts - **blog**, **blog posts** and **admin blog management activities**.
* this is a very simple blog feature whose purpose it to give customers more than just a shopping experience while navigating through ECOSiO.
* **blog** displays short introductions to all available **blog posts** and links to them.
* **blog posts** are individual blog entries, each tackling a topic related to sustainability and/or eco-friendly cosmetics. The topics are ideally chosen based on the questions coming from the users and aim to showcase one of the external brands ECOSiO has been working with. Through this brand partnership, ECOSiO gives a chance to the external brands for an additional marketing exposure.
* **admin blog management activities** include adding, editing and deleting blog entries. Users with admin rights can do that directly in the UI through forms. In case of deleting a blog post, a **modal** will open to double check if the user really wants to do this irreversible action.

![Blog Page Features](readme-files/img-features/img-features-blog.png)

**Loyalty programme app**
* `loyalty_programme` Django app is also one of the apps that are mostly relying on textual content.
* this page explains how the programme actually works from user's perspective and what are the benefits of joining the programme, i.e. creating an account.
* the purpose of this feature is to offer an incentive for an account creation and maintain an on-going relationship with the loyal customers through rewards and other benefits.
* the logic of the programme is implemented under `profile` app since it's closely related to the `UserProfile` model. You can read more about it below, under `profiles` app.

![Loyalty programme Features](readme-files/img-features/img-features-loyalty-programme.png)

**Products app, i.e. Webshop**
* `products` Django app is where all the logic and templates connected to the product feed and individual products are.
* it can be divided into three main sections: **shop**, **product pages** and **admin product management activities**.
* **shop** is the main feed of products and this is where the majority of shopping journeys are expected to start. The shopping experience is enhanced by having a **dropdown for sorting products** (A-Z, Z-A, price low-high, price high-low), **category filters** (skincare, shaving, toiletries, sets & bags) and **product tag filters** that follow the user across the desktop version of the page and a quick **add-to-cart** functionality for users that already know exactly what they want to buy.
* **product pages** are pages dedicated to each individual product. On these pages, the users can **read the product description, find ingredient list of the product** as well as **get additional product recommendations**. The product recommendations are random. The system selects 3 products from the same category the main product on the page belongs to and displays them at the bottom of the page. The recommended products turn into a scrollable gallery similar to the one on the homepage.
* additional feature on the product pages are **product tags** which help with deciding whether a product fits certain lifestyle or not. There are 5 tags in total - **eco-friendly** which is a tag all ECOSiO's products should have, and then **cruelty-free**, **100% vegan**, **100% organic** and **100% natural**. Users can also filter the products based on these tags in the **shop**.
* **admin product management activities** include adding, editing and deleting products. Users with admin rights can do that directly in the UI through forms. In case of deleting a product, a **modal** will open to double check if the user really wants to do this irreversible action.

![Shop Features](readme-files/img-features/img-features-shop.png)

**Cart app**
* `cart` Django app is a standard e-commerce functionality which aids the checkout process.
* a cart is always present in the top right corner of the web app. **It turns black if it's full and shows the number of items added to the cart**.
* currently, a customer can put **up to 99 items of the same product** into the cart. If the user tries to add more items than that, the system alerts the user via toasts that 99 items is the maximum number of products that can be added.
* however, **adding products to the cart works differently on the product pages**. The users can define the exact amount of products they want to put into the cart as long as it's within the range (1 to 99). Since products can also be added from the homepage and the shopping feed, it might happen that the user has already added, for example, 10 items of the same product into the cart and now is trying to add 95 more products from the product page on top of that. The system will in that case check if the the sum of the current amount in the cart and the desired additional amount is higher than the allowed limit and **limit the amount of this same product in the cart to 99** if needed.
* after clicking on the cart in the top right corner, the users gets an overview of all the products put into the cart. The user can also modify the quantity of the added products as well as remove the products from the cart. Since removing products from the cart is not an irreversible action, I have decided not to have a modal here so that the focus remains on the checkout process.
* all the products in the cart are also linked to their product pages so that the users have an easy acces to them in case they wish to check them out again before entering the checkout process.
* the information provided on this page includes **usual product information, quantity per product, costs per product, order costs** (with 10% discount for first-time registered buyers), **shipping costs** (free for orders worth 120.00€ and above, as well as level 2 and level 3 loyal customers - otherwise 4.00€) and **total order costs**.
* if users try to access their empty carts, there will be a message displayed that nothing has been added yet and encourage them to go to the shop.

![Cart Features](readme-files/img-features/img-features-cart.png)

**Checkout app**
* `checkout` Django app is another standard e-commerce functionality which enables users to buy the products online from the webshop.
* in order to check out, the user is presented with a **form asking for the shipping and payment details** and the **overview of the order**.
* users can easily go back to the cart and adjust it by clicking on the cart in the top right corner or breadcrumbs in the top left corner.
* all the discounts or benefits will also be visible and highlighted in the summary of the costs.
* both registered and anonymous users can shop at ECOSiO. Logged in users will have an option to **save their information** to the profile which should populate the form with relevant details for the next purchase.
* a webhook is implemented to the `checkout` so that the order is successfully processed in case the checkout process gets interrupted. Some reasons might be closing the browser too soon or losing internet connection.
* "payments" are handled through `stripe`. A test purchase can be made with the following details:
    * **credit card:** 4242 4242 4242 4242
    * **expiration date:** 04 / 24
    * **CVC:** 424
    * **ZIP:** 42424
* after the payment has been processed, the user is presented with the order summary on the **order confirmation page**.
* logged in buyers can also see their **order history** on the `profiles` pages.

![Checkout Features](readme-files/img-features/img-features-checkout.png)

**Profiles app - and Loyalty Programme feature**
* `profiles` Django app is available to registered, authenticated users.
* it offers 3 features: **order history**, **saving shipping information** and **loyalty programme**.
* **order history** displays all previous orders per user account.
* **saving shipping information** is done through a form which can be edited any time. This information is what populates the checkout form for the next orders.
* **loyalty programme** is a feature that is partially implemented in the `profiles` app and partially in the `checkout` app. There are three levels users can achieve and unlocking each level brings new benefits. This is how the logic is distributed between the `checkout` and `profiles` app
    * `profiles` app: **stores loyalty points** under `UserProfile` model. It distinguishes between:
        - `earned_loyalty_points` - received after a purchase has been made. All the donated points get excluded from `earned_loyalty_points`.
        - `donated_loyalty_points` - sum of points donated by the user to one of the three causes.
            - `donated_loyalty_points_plant_tree` - points donated for planting a tree.
            - `donated_loyalty_points_recycle_plastic` - points donated to aid plastic recycling.
            - `donated_loyalty_points_clean_forest` - points donated to aid cleaning forests.
        - `total_loyalty_points` - all earned points ever received (earned and donated points together).
    * `checkout` app: **10% off the first purchase** for newly registered users. It is applied to users with no loyalty points. The free delivery threshold has been adjusted to follow the discounted order total.
    * `checkout` app: **1 loyalty point each time 10.00€ is spent**. Shipping costs are not included in the calculation.
    * `checkout` app: **free delivery for level 2 and level 3 users** is handled by overriding delivery costs if user has reached a certain number of points.
    * `profiles` app: **keeps track of users' loyalty statuses** by informing how many points are needed to unlock the next level, how many points have been donated to good causes, what are the benefits currently available to the users and which ones will be unlocked in the future.
    * `profiles` app: **registration for attending ECOSiO's live event**. Level 3 customers can register for an event that ECOSiO holds once a year. This feature is suppose to help with strengthening the community built around the brand and it's a chance for customers to meet the team and like-minded people.

![Profiles Features](readme-files/img-features/img-features-profiles.png)

