# How to add your CoFI example here

Thanks for considering contributing!

Adding your own example into the list is easy. You only need to provide three things,
a link to your working example (either a notebook or a script), a link to a thumbnail 
image for preview purposes, and a title.

Once you have the three things ready, provide them to us either through 
[submitting an issue](CONTRIBUTE.md#submit-through-a-github-issue) or 
[raising a pull request](CONTRIBUTE.md#submit-through-a-github-pull-request).

## Submit through a GitHub issue

1. Navigate to [the issue creation page](https://github.com/inlab-geo/cofi-gallery/issues/new?assignees=&labels=new+example&template=add-new-example.md&title=Add+%60My+Cool+Example%60)
2. Fill in the information and tick on the checklist
3. Click "Submit new issue"

We will contact you if needed. Otherwise you will get a notification that your 
example is successfully updated to CoFI gallery once this issue is closed by us.

## Submit through a GitHub pull request

1. Fork and clone this repository 
   ```console
   $ git clone https://github.com/<your_github_account>/cofi-gallery.git
   ```
2. Create an empty yaml file from template
   ```console
   $ pip install -r requirements.txt
   $ python tools/new_example.py <my_cool_example>
   ```
3. Go to `gallery/<my_cool_example>.yml` to fill insert necessary information
4. Push to your fork
   ```console
   $ git add gallery/<my_cool_example>.yml
   $ git commit -m "Add <my_cool_example>"
   $ git push origin main
   ```
5. Navigate to `https://github.com/<your_github_account>/cofi-gallery.git` from your 
   browser and click on "Contribute" "Open pull request" and continue to submit 

We will contact you if needed. Otherwise you will get a notification that your 
example is successfully updated to CoFI gallery once this pull request is merged by
us.

