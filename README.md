# **Task Description:**

**Fruitipedia App - Python Web Basics Exam**

*The app allows the user to browse different fruits including their nutrition info, description, name, and image. The user can create, edit, or delete fruits at any time. He/ She can also edit or delete his/ her profile.*
## **Skeleton**
You are provided with all the needed **HTML pages**, **images,** and **CSS** files for the project.
## **Database**
You will need **2 models**:
- ### **Profile Model**
  - **First Name**
    - Character field, **required.**
    - It should consist of a **maximum of 25 characters and** a **minimum of 2 characters.**
    - The first name **must start with a letter**. Otherwise raise **ValidationError** with the following message: "**Your name must start with a letter!**"
  - **Last Name**
    - Character field, **required.**
    - It should consist of a **maximum of 35 characters and** a **minimum of 1 character.**
    - The last name **must start with a letter**. Otherwise raise **ValidationError** with the following message: "**Your name must start with a letter!**"
  - **Email**
    - Email field, **required**.
    - It should consist of a **maximum** **of 40 characters.**
  - **Password**
    - Character (password) field, **required**.
    - It should consist of a **maximum of 20 characters and** a **minimum** **of 8 characters.**
  - **Image URL**
    - URL field, **optional**.
  - **Age**
    - Integer field, **optional**.
    - The age **default value should be 18**.

- ### **Fruit Model**
  - **Name**
    - Character field, **required.**
    - It should consist of a maximum of **30 and** a **minimum of 2 characters**.
    - The name should contain **only letters**. Otherwise raise a **ValidationError** with the following message: "**Fruit name should contain only letters!**"
  - **Image URL**
    - URL field, **required.**
  - **Description**
    - Text field, **required.**
  - **Nutrition**
    - Text field, **optional.**

**Note: the project will be examined only on the user side; models will NOT be tested on the admin site with a superuser profile.**
## **Routes**
- <http://localhost:8000/> - index page
- <http://localhost:8000/dashboard/> - dashboard page
- <http://localhost:8000/create/> - fruit create page
- [http://localhost:8000/<fruitId>/details/](http://localhost:8000/%3cfruitId%3e/details/) - fruit details page
- [http://localhost:8000/<fruitId>/edit/](http://localhost:8000/%3cfruitId%3e/edit/) - fruit edit page
- [http://localhost:8000/<fruitId>/delete/](http://localhost:8000/%3cfruitId%3e/delete/) - fruit delete page
- <http://localhost:8000/profile/create>/ - profile create page
- <http://localhost:8000/profile/details/> - profile details page
- <http://localhost:8000/profile/edit/> - profile edit page
- <http://localhost:8000/profile/delete/> - profile delete page


## **Pages**:
-----------------------------------
## 1. **Index page**
**Template file**: **"index.html"**

The page consists of:

- A **navigation bar** with:
- **"Fruitipedia"** link, which leads to the **index** page.
- **"Create Profile"** link, which leads to **create profile** page.
- **"Dashboard"** link, which leads to the **dashboard** page.
- **"Add Fruit"** link, which leads to the **create fruit** page.
- **"Profile"** link, which leads to the **profile details** page.

Keep in mind that the **"Create Profile"** link on the navigation bar is **only visible** when the user **has NOT created a profile yet**: 

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.001_vi2wj0.png)

The **"Dashboard"**, **"Add Fruit"**, and **"Profile"** links on the navigation bar are **only visible** when the user **has a profile:**

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.002_qbifpy.png)

## 2. **Create Profile Page**
**Template file**: **"create-profile.html"**

The page consists of:

- A **navigation bar** with:
- **"Fruitipedia"** link, which leads to the **index** page.
- **"Create Profile"** link, which leads to **create profile** page.
- A **profile** **creation form** consisting of:
- A **"First Name"** field, a placeholder **"First Name"** and **no label**
- A **"Last Name"** field, a placeholder **"Last Name"** and **no label**
- An **"Email"** field, a placeholder **"Email"** and **no label**
  - A **"Password"** field, a placeholder **"Password"** and **no label** (When the user enters his/her password, the symbols could be **hidden or visible**)
- A button **"Create"**
- When you **click** on it **if** the profile is **successfully created**, you should be redirected to the **dashboard page**.
- Otherwise, the form should show the **appropriate validation errors in the form**.

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.003_xox6z2.png)

## 3. **Dashboard Page**
**Template file**: **"dashboard.html"**

The **dashboard page shows all fruits which have been created by the user.** 

If there are **no fruits created yet**, the page should have the following:

- A navigation bar, as shown below.
- A heading **"No fruit info yet"**

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.004_czoibt.png)

If the **user** **has some** **fruits,** the page should have the following:

- A navigation bar, as shown below.
- A division for each fruit, showing:
- The fruit's **image**
- The fruit's **name**
- The fruit's **description**. The description should show **only** **the first 50 characters!**
- A **button** **"More Info"** leading to the **details page** for the selected fruit

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.005_khwwkb.png)
## 4. **Create Fruit Page**
Template file: **"create-fruit.html"**

The page consists of:

- A **navigation bar,** as shown below.
- A **fruit** **creation form** consisting of:
- A **"Name"** field, a placeholder **"Fruit Name"** and **no label**
- An **"Image URL"** field, a placeholder **"Fruit Image URL"** and **no label**
- A **"Description"** field, a placeholder **"Fruit Description"** and **no label**
- A **"Nutrition"** field, a placeholder **"Nutrition Info"** and **no label**
- A button **"Add Fruit"**
- When you **click** on it **if** the fruit is **successfully created**, you should be redirected to the **dashboard page**.
- Otherwise, the form should show the **appropriate validation errors**.
**


![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.006_utgafl.png)

## 5. **Fruit Details Page**
Template file: **"details-fruit.html"** 

This page contains a fruit’s information. It should have the following:

- The **fruit's image**
- The **fruit's name**
- The **fruit's description**
- The **fruit's nutrition info**, starting with a **paragraph "Nutrition"** (**visible** even if there is **no** nutrition info)
- An **"Edit"** button that leads to the **edit fruit page**
- A **"Delete"** button that leads to the **delete fruit page**

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.007_dudqcc.png)


## 6. **Edit Fruit Page**
Template file: **"edit-fruit.html"**

On the page, the form must be **filled** with **information** about the **fruit** we want **to edit.** Each field has **a label: "Name:"**, **"Image URL:"**, **"Description:"**,** and **"Nutrition:"**.

When you click on the **"Edit"** button:

- **If** the fruit is **successfully edited**,** you should be redirected to the **dashboard** **page**.
- **Otherwise**, the form should show the **appropriate validation errors**.

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.008_ryzldq.png)
## 7. **Delete Fruit Page**
Template file: **"delete-fruit.html"**

On the page, the form must be **filled** with the **fruit's information**, and **all the fields** should be **disabled.** Each field has **a label: "Name:"**, **"Image URL:"** and **"Description:"**.

When you click on the **"Delete"** button, the **fruit** is **deleted from the database**, and you should be redirected to the **dashboard page**.

The deleted fruit should be **no longer visible in the app**.

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612444/b3d697d6-e091-43be-a041-e2c5ee87fcf8.009_u9dovw.png)
## 8. **Profile Details Page**
Template file: **"details-profile.html"**

This page contains the **user's information**. It should have the following:

- A **profile** **picture**. If **no picture is given**, the page should show a **default profile picture** (in the static/image folder)
- **First name** and **last name**:
- The **email**
- The **age**
- The **total number of posts** that the user has. Display **0**(zero) if there are **no** **posts**.
- An **"Edit"** button that leads to the **edit profile page**
- A **"Delete"** button that leads to the **delete profile page**

**If the user has a profile picture:**

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.010_d8izzc.png)

**If the user doesn't have a profile picture:** 

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.011_innnjf.png)
## 9. **Edit Profile Page**
Template file: **"edit-profile.html"**

On the page, the form must be **filled** with the **information** of the **profile** we want **to edit. The profile** **edition form** has **additional fields as shown below**:

- A **"First Name:"** field
- A **"Last Name:"** field
- An **"Image URL:"** field
- An **"Age:"** field

All fields have **labels**.

When you click on the **"Edit"** button:

- **If** the profile is **successfully edited**,** you should be redirected to the **profile details page**.
- **Otherwise**, the form should show the **appropriate validation errors**.

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612443/b3d697d6-e091-43be-a041-e2c5ee87fcf8.012_jflbd3.png)


## 10. **Delete Profile Page**
Template file: **"delete-profile.html"**

Deleting a profile should delete the profile info and **all of his /her added fruits.** After **deletion**, the user should be redirected to the **index page**.

![](https://res.cloudinary.com/dpu6f6jc5/image/upload/v1687612444/b3d697d6-e091-43be-a041-e2c5ee87fcf8.013_rpsfut.png)

