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

### App Sections

1. **Navigation at the top** - fixed on the top so that the users are able to navigate themselves anytime. It consists of two HTML code snippets for better responsiveness handling. The top navigation is a combination of a brand logo, search box, account related activities and the cart functionality. The navigation below is present for navigating throughout the main app sections.
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
