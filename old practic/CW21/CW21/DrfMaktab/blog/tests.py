from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse

from blog.models import Post, Tag
from model_mommy import mommy

User = get_user_model()


class TestPost(APITestCase):

    def setUp(self):
        # user = User(username='dev', password='123')
        # user.save()
        # post1 = Post(title='post title1', creator=user, published=True)
        # post1.save()
        # post2 = Post(title='post title2', creator=user)
        # post2.save()
        # post3 = Post(title='post title3', creator=user, published=True)
        # post3.save()

        self.user = mommy.make(User)
        mommy.make(Post, published=True, creator=self.user, _quantity=10)
        mommy.make(Post, published=False, _quantity=5)

        mommy.make(Tag, _quantity=2)

    def test_post_list(self):
        url = reverse('post_list')
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 10)

    def test_create_post(self):

        url = reverse('post_list')

        tag = Tag.objects.first()
        data = {
            'title': 'test title',
            'tag': tag.id
        }
        self.client.force_authenticate(self.user)

        resp = self.client.post(url, data=data)

        self.assertEqual(resp.status_code, 201)

        post = Post.objects.get(id=resp.data['id'])

        self.assertEqual(post.creator, self.user)
        self.assertFalse(post.published)

    def test_update_post(self):
        post = Post(creator=self.user, title='test title', tag=Tag.objects.first())
        post.save()

        url = reverse('post_detail', kwargs={'id':post.id})
        new_title = "new title"
        data = {
            "title": new_title,
            "tag": Tag.objects.last().id
        }

        self.client.force_authenticate(self.user)
        resp = self.client.put(url, data)

        self.assertEqual(resp.status_code, 200)

        updated_post = Post.objects.get(id=post.id)
        self.assertEqual(updated_post.title, new_title)

    def test_update_post_with_invalid_user(self):
        post = Post(creator=self.user, title='test title', tag=Tag.objects.first())
        post.save()

        url = reverse('post_detail', kwargs={'id': post.id})
        new_title = "new title"
        data = {
            "title": new_title,
            "tag": Tag.objects.last().id
        }

        another_user = mommy.make(User)
        self.client.force_authenticate(another_user)

        resp = self.client.put(url, data)

        self.assertEqual(resp.status_code, 404)