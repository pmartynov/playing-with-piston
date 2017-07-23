# git+https://github.com/pmartynov/piston-lib.git@master#egg=piston-lib
from piston.steem import Steem

username = '' # fill
posting_key = '' # fill

STEEM_NODE = 'wss://steemd.steemit.com'
GOLOS_NODE = 'wss://ws.golos.io'


# curl https://ws.golos.io --data '{"method": "call", "params": ["login_api", "get_api_by_name", ['follow_api']], "id": 0}'
# curl https://ws.golos.io --data '{"method": "call", "params": ["database_api", "get_discussions_by_created", [{"limit": 1, "offset": null}]], "id": 0}'


def upvote_last_post(steem_obj):
    limit, offset = 1, None
    query = dict(limit=limit, offset=offset)
    posts = steem_obj.rpc.get_discussions_by_created(query)
    for post in posts:
        identifier = '@%s/%s' % (post['author'], post['permlink'])
        steem_obj.vote(identifier, 10, username)


def create_new_post(steem_obj):
    meta = {'extensions': [[0, {'beneficiaries': [{'account': 'pmartynov', 'weight': 1000}]}]], 'app': 'super-duper-upvotebot/0.0.1',}
    author = username
    title = 'asdfasdf123'
    tags = ['test', 'tag']
    body = 'some text'

    steem_obj.post(meta=meta, author=author, title=title, tags=tags, body=body)


def create_new_comment(steem_obj):
    meta = {'extensions': [[0, {'beneficiaries': [{'account': 'pmartynov', 'weight': 1000}]}]], 'app': 'super-duper-upvotebot/0.0.1',}
    author = username
    title = 'asdfasdf123'
    identifier = '@gabrielvlad/22mt7r-red-roses'
    body = 'some text'

    steem_obj.reply(meta=meta, author=author, title=title, body=body, identifier=identifier)


def follow(steem_obj):
    # "blog" to follow the person, "ignore" to mute the person, and an empty string ("") to unfollow the person.
    steem_obj.follow('dan', ['blog'], username)


def unfollow(steem_obj):
    steem_obj.unfollow('dan', [], username)


if __name__ == "__main__":
    steem_obj = Steem(node=STEEM_NODE, wif=posting_key)
    create_new_comment(steem_obj)
    upvote_last_post(steem_obj)
    create_new_post(steem_obj)
    follow(steem_obj)
    unfollow(steem_obj)
