# Pokemon-ID Project
By William Norton Jr

## Overview


## Data

The images for this project were initially sourced from two Kaggle datasets ([first](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types?select=images), [second](https://www.kaggle.com/datasets/kvpratama/pokemon-images-dataset)), totaling 1500 images.  [A third Kaggle dataset](https://www.kaggle.com/datasets/rounakbanik/pokemon?resource=download) was used to bring in a csv with stats about Pokemon.  I knew I would need more images to train effective models, so I decided to webscrape off of Pokemondb.  I used a combination of Python, BeautifulSoup, and Selenium to first get the image urls and then download them into a folder for each Pokemon.  Next, I sorted the images from the Kaggle datasets into those folders.  Then I sorted the folders for individual Pokemon into folders based on the Pokemon’s primary type. Lastly, I manually added stats from Pokemondb’s Pokedex for a handful of Pokemon that were missing from the stats csv file.

## Modeling

I used this guide from Google as a starting point, using keras and tensorflow to train models to first identify the primary type of Pokemon.  Based on the type of Pokemon, a second model was then used to identify the individual Pokemon.  For both the initial model and the follow-up I selected accuracy as the most appropriate metric.  I modified code from this post in order to split the test images into train/validation/test datasets.  To avoid class imbalance issues, I dropped the Flying type, as only three Pokemon had that as their primary type.  This left 809 Pokemon divided among 17 different primary types.

After implementing the first simple model based on the Google template, I iteratively implemented tweaks and different techniques in an attempt to boost the model’s accuracy.  Techniques that were tried included back transmission, image augmentation, a variety of batch size & epochs, and introducing dropout layers.  Ultimately, the most accurate model on the validation data was relatively similar to the FSM, but with several more drop-out layers, which helped it avoid overfitting on the training data.  Next a model was trained for each type to identify the individual Pokemon within that type.  These models used identical designs based on the best first stage model, but with slightly increased drop-out in order to limit overfitting on the smaller datasets.

## Results

The results on the unseen test data was strong, with over 90% accuracy for identifying the type of Pokemon.  The second stage models ranged in accuracy from 85-95%.  Taken together, the app should have roughly 80% accuracy at getting both right.  

Unfortunately, testing on other images of Pokemon from the internet and of photos of Pokemon stuffed animals in real life revealed some limitations.  The images used to train the models and the holdout test images all have one Pokemon that is centered with a transparent background.   As a result, the app struggles with more complex images.

## The App

I used Streamlit to create and deploy an app that utilized the models <br>
[App Github Repo](https://github.com/Noptov/Pokemon-App), [Pokemon ID Project App](https://share.streamlit.io/noptov/pokemon-app/main/pokeid-app.py)

## Future Steps

There are several steps I want to take to improve the Pokemon ID Project.  Firstly, my model does not currently account for backgrounds.  This can cause the app to struggle on real world images.  It also does not account for multiple pokemon in one image.  Incorporating checks for these could greatly improve accuracy on a more diverse array of images.  Secondly, I have only trained models for pokemon through generation seven and would like to add generation eight and later in 2022, generation nine.  Lastly,  I would like to use 

## Repo Tree

```
📦 
├─ Data/
├─ Models/
├─ Streamlit-App/
├─ .gitattributes
├─ .gitignore
├─ Models-ID-Pokemon.ipynb
├─ README.md
├─ Stats_data_cleaning.ipynb
├─ Type Model.ipynb
├─ image-scraper.ipynb
└─ png-convert.ipynb
```