# Testing and Defensive Design

## Defensive Design and Predicted Error Points

In this chapter I will focus more on which steps I've taken to prevent predicted errors and complications. In the beginning I focused
more on the actions that could break the site or site structure completely, and afterwards more on restrictions that would make
sense for this project in general.

1. Custom Error Webpages
* includes error 400, 403, 404 and 500
* since errors do happen anyways, no matter how well the defensive design has been thought through, I believe custom error pages are better for the user experience
* these pages inform the user of the error that has just happen but at the same time don't disrupt the user's mindset by a sudden change of environment (brand-friendly to foreign page design) and they support user's journey throughout the app better (by having links to return to other parts of the web app)

2. Secured Admin Views
* admin-related activities happening on the site, such as adding, editing and deleting products or blog posts - are secured for superusers
* if a user still tries to access those pages, they are redirected to the homepage with a toast saying that only ECOSiO's team is allowed to do these actions
* this has been done by:
    * importing `@login_required` decorator in `views.py` files
    * redirecting to the homepage
    * displaying error toast message

![Secured Admin Views](readme-files/img-testing/img-testing-admin-rights.png)

3. Modals When Permanently Deleting Data
* some admin-related activities such as deleting products and blog posts are permanent
* a modal will pop up to double check whether a user really wants to do such action or not
* when it comes to removing items from the cart, no modal appears since this is not a permanent action and products can easily be re-added to the cart

![Modals](readme-files/img-testing/img-testing-modal.png)

4. Search Queries Safe for Site Structure
* firstly, if the query is an empty string, users are redirected to the webshop with a toast message
* I've also taken care of long search queries without white spaces or search queries that are simply too long and could break the site's responsiveness and structure
* for that reason, the following actions have been taken:
    * search box `<input>` is restricted to `maxlength="50"`
    * search term in breadcrumbs is restricted to `{{ search_term|truncatechars:25 }}`
    * search term length on the page is limited by `{{ search_term|truncatechars:50 }}`
* this also helps with link manipulation demonstrated below, in case users try to type the search query directly in the link so that the restrictions mentioned earlier are avoided

![Search Query Link Manipulation](readme-files/img-testing/img-testing-search-link-manipulation.png)

5. Maximum Items per Order - 150
* a user can order up to 150 items per order
* the code can be found in `views.py` in the `cart` app
* in short, the system sums the quantity of items that are already in the cart with the quantity that is being submitted to the limit of 150 items in total per cart
* if the calculated potential sum is higher than the limit, the users get a toast message after being redirected to the same page they were on previously
* an example of this error would be when there are 140 products in the cart and the user tries to add 20 more items (new total would be 160 which is higher than the limit of 150)

![Max 150 Items per Order](readme-files/img-testing/img-testing-cart-max-150.png)

6. Maximum Same Products per Order - 99
* when it comes to individual products per order, a user can order up to 99 same items
* products can be added to the cart at 4 places within the web app:
    * by clicking 'add to cart` button on the homepage ('our most popular products' section)
    * by clicking 'add to cart` button in the webshop's product feed (product cards)
    * by adding products through the input field on the product page (+/- input field that)
    * by clicking 'add to cart` button on the product page ('recommended for you' section)
* the code can be found in `views.py` in the `cart` app
* in short, the system checks if the product's ID is already in the cart, takes it's quantity, sums it with the quantity that is being submitted and compares it to the limit of 99 same items per order
* if the amount is higher than 99, and the general limit of maximum 150 products per order hasn't been reached, the system changes the current quantity to maximum 99 items in the cart and alerts the user of the changes
* an example of this error would be when there are 89 products in the cart already and the user tries to add 20 more on top of that through the product page input box (new total would be 109 which is higher than the limit of 99)

![Max 99 Same Items per Order](readme-files/img-testing/img-testing-cart-max-99.png)

7. User-Frienly Product Page Input
* product pages work a bit differently when it comes to adding products to the cart than the 'add to cart' buttons
* 'add to cart' buttons will increase the quantity of the product by 1, while on product pages, users can submit a bulk number which might be prone to Manipulation
* for that reason, the following actions have been taken:
    * the `<input>` tag takes in only numbers as value (`type="number"`) between `min="1"` and `max="99"`
    * if users try to submit empty value, they are redirected to the product page with a toast message

![Product Page Input Manipulation](readme-files/img-testing/img-testing-product-page-input-manipulation.png)

8. Cart Adjustments
* similar code has been implemented in the `cart` app as well - a user can't adjust a product's quantity to higher than 99 nor exceed the 150 products in total per order
* however, if users 'update' the cart item to the same number, a toast message appears informing them no changes have been made
* since no errors have technically been made here, I thought this might be a small help in case the user actually tried to change the amount of the product but ended up with the same amount anyhow
* the code can be found in `views.py` in the `cart` app

9. Product and Blog Images
* additional precautions were taken when uploading new products and blog posts
* new products have image as an optional field in their model - if there is no image uploaded, a generic `no_image.png` is used as a placeholder
* when it comes to blogs, their images are also header images, so I've made that a mandatory field in the model
* it could happen that the blog image gets deleted from AWS bucket for example - if that happens a simple JavaScript code replaces the images with a `no_image_blog.png` file
```bash
// handle broken blog header images
$('.blog-header-image').on("error", function() {
    $(this).attr('src', '/media/no_image_blog.png');
});
```

10. Manipulating Loyalty Points Donation
* registered users that have collected at least 61 loyalty points and unlocked level-2 feature of donating points might try to manipulate this feature
* the users donate points by clicking on the cause they want to contribute to
* the same could be done by typing links into the browser, such as:
    * `http://ecosio.herokuapp.com/profile/donate_plant_tree/`
* this particular action would donate 2 loyalty points to planting a tree with ECOSiO
* users could potentially try to keep on 'donating' their points until they reach either points in negative values, or 0 - which would be their access to a new 10% discount valid only for first orders, i.e. users with no loyalty points
* this has been handled in `profiles` app`views.py` file, where a rule has been added that you cannot donate points if you have less than 61 points
* this way a user can still make donations by typing a link but at least it's not possible to do this endlessly, the feature is available to only level-2 and level-3 users as imagined and, in the end, the user is only losing their own points and benefits - so hopefully no one would want to do this to themselves anyways in the first place
* if users with less than 61 loyalty points try to access the donations via link, the system redirect them to the same page and shows a toast message informing them they don't have enough points to do the action