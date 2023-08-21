import requests,json
class Client():
	def __init__(self,token):
		self.token=token
		self.api=f"https://api.telegram.org/bot{self.token}"
	def get_Me(self):
		return requests.get(f"{self.api}/getMe").json()
	def logout(self):
		return requests.get(f"{self.api}/logOut").json()
	def get_File(self,fileId:str):
		return requests.get(f"{self.api}/getFile?file_id={fileId}").json()
	def send_message(self,chat_id:str, text:str,disable_web_page_preview:str=None, reply_to_message_id:str=None,parse_mode:str=None, disable_notification:str=None, timeout:str=None, allow_sending_without_reply:str=None, protect_content:str=None,message_thread_id:str=None):
		data={'chat_id': chat_id, 'text': text}
		if disable_web_page_preview:data['disable_web_page_preview'] = disable_web_page_preview
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if parse_mode:data['parse_mode'] = parse_mode
		if disable_notification:data['disable_notification'] = disable_notification
		if timeout:data['timeout'] = timeout
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendMessage",json=data).json()
	def set_webhook(self,url=None, max_connections=None, allowed_updates=None, ip_address=None,drop_pending_updates = None, timeout=None, secret_token=None):
		data={'url':""}
		if url: data["url"]=url
		if max_certificate:data['max_connections'] = max_connections
		if allowed_updates:data['allowed_updates'] = json.dumps(allowed_updates)
		if ip_address:data['ip_address'] = ip_address
		if timeout:data['timeout'] = timeout
		if secret_token:data['secret_token'] = secret_token
		if drop_pending_updates:data['drop_pending_updates'] = drop_pending_updates
		return requests.post(f"{self.api}/setWebhook",json=data).json()
	def delete_webhook(self,drop_pending_updates=None, timeout=None):
		data={}
		if drop_pending_updates:data["drop_pending_updates"]=drop_pending_updates
		if timeout:data["timeout"]=timeout
		return requests.post(f"{self.api}/deleteWebhook",json=data).json()
	def unhide_general_forum_topic(self,chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/unhideGeneralForumTopic",json=data).json()
	def hide_general_forum_topic(self,chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/hideGeneralForumTopic",json=data).json()
	def reopen_general_forum_topic(self,chat_id):
		data ={'chat_id': chat_id}
		return requests.post(f"{self.api}/reopenGeneralForumTopic",json=data).json()
	def close_general_forum_topic(self,chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/closeGeneralForumTopic",json=data).json()
	def edit_general_forum_topic(self,chat_id,name):
		data={'chat_id': chat_id, 'name': name}
		return requests.post(f"{self.api}/editGeneralForumTopic",json=data).json()
	def stop_poll(self,chat_id,message_id):
		data={'chat_id': str(chat_id), 'message_id': message_id}
		return requests.post(f"{self.api}/stopPoll",json=data).json()
	def get_forum_topic_icon_stickers(self):
		return requests.get(f"{self.api}/getForumTopicIconStickers").json()
	def unpin_all_forum_topic_messages(self, chat_id, message_thread_id):
		data={'chat_id': chat_id, 'message_thread_id': message_thread_id}
		return requests.post(f"{self.api}/unpinAllForumTopicMessages",json=data).json()
	def delete_forum_topic(self, chat_id, message_thread_id):
		data={'chat_id': chat_id, 'message_thread_id': message_thread_id}
		return requests.post(f"{self.api}/deleteForumTopic",json=data).json()
	def get_webhook_info(self,timeout=None):
		data={}
		if timeout:data['timeout'] = timeout
		return requests.post(f"{self.api}/getWebhookInfo",json=data).json()
	def get_updates(self, offset=None, limit=None, timeout=None, allowed_updates=None, long_polling_timeout=None):
		data={}
		if offset:data["offset"]=offset
		if limit:data["limit"]=limit
		if timeout:data["timeout"]=timeout
		if long_polling_timeout:data["long_polling_timeout"]=long_polling_timeout
		if allowed_updates:data["allowed_updates"]=json.dumps(allowed_updates)
		return requests.post(f"{self.api}/getUpdates",json=data).json()
	def reopen_forum_topic(self,chat_id, message_thread_id):
		data={'chat_id': chat_id, 'message_thread_id': message_thread_id}
		return requests.post(f"{self.api}/reopenForumTopic",json=data).json()
	def send_poll(self,chat_id,question,is_anonymous = None, type = None, allows_multiple_answers = None, correct_option_id = None,explanation = None, explanation_parse_mode=None, open_period = None,is_closed = None,disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=None,timeout=None, explanation_entities=None, protect_content=None, message_thread_id=None):
		data = {'chat_id': chat_id,'question': question}
		if is_anonymous:data['is_anonymous'] = is_anonymous
		if type:data['type'] = type
		if allows_multiple_answers:data['allows_multiple_answers'] = allows_multiple_answers
		if correct_option_id:data['correct_option_id'] = correct_option_id
		if explanation:data['explanation'] = explanation
		if explanation_parse_mode:data['explanation_parse_mode'] = explanation_parse_mode
		if open_period:data['open_period'] = open_period
		if is_closed:data['is_closed'] = is_closed
		if disable_notification:data['disable_notification']=disable_notification
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if timeout:data['timeout'] = timeout
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendPoll",json=data).json()
	def create_forum_topic(self, chat_id, name, icon_color=None, icon_custom_emoji_id=None):
		data={'chat_id': chat_id, 'name': name}
		if icon_color:data['icon_color'] = icon_color
		if icon_custom_emoji_id:data['icon_custom_emoji_id'] = icon_custom_emoji_id
		return requests.post(f"{self.api}/createForumTopic",json=data).json()
	def close_forum_topic(self, chat_id, message_thread_id):
		data={'chat_id': chat_id, 'message_thread_id': message_thread_id}
		return requests.post(f"{self.api}/closeForumTopic",json=data).json()
	def edit_forum_topic(self, chat_id, message_thread_id, name=None, icon_custom_emoji_id=None):
		data={'chat_id': chat_id, 'message_thread_id': message_thread_id}
		if name:data['name'] = name
		if icon_custom_emoji_id:data["icon_custom_emoji_id"]=icon_custom_emoji_id
		return requests.post(f"{self.api}/editForumTopic",json=data).json()
	def get_user_profile_photos(self, user_id, offset=None, limit=None):
		data={'user_id':user_id}
		if offset:data["offset"]=offset
		if limit:data["limit"]=limit
		return requests.post(f"{self.api}/getUserProfilePhotos",json=data).json()
	def get_chat(self,chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/getChat",json=data).json()
	def leave_chat(self, chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/leaveChat",json=data).json()
	def get_chat_administrators(self, chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/getChatAdministrators",json=data).json()
	def get_chat_member_count(self,chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/getChatMemberCount",json=data).json()
	def set_sticker_set_thumbnail(self, name, user_id, thumbnail):
		data={'name': name, 'user_id': user_id,'thumbnail':thumbnail}
		return requests.post(f"{self.api}/setStickerSetThumbnail",json=data).json()
	def set_chat_sticker_set(self,chat_id, sticker_set_name):
		data={'chat_id': chat_id, 'sticker_set_name': sticker_set_name}
		return requests.post(f"{self.api}/setChatStickerSet",json=data).json()
	def delete_chat_sticker_set(self,chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/deleteChatStickerSet",json=data).json()
	def get_chat_member(self, chat_id, user_id):
		data={'chat_id': chat_id, 'user_id': user_id}
		return requests.post(f"{self.api}/getChatMember",json=data).json()
	def forward_message(self, chat_id, from_chat_id, message_id,disable_notification=None, timeout=None, protect_content=None, message_thread_id=None):
		data={'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
		if disable_notification:data['disable_notification'] = disable_notification
		if timeout:data['timeout'] = timeout
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/forwardMessage",json=data).json()
	def copy_message(self, chat_id, from_chat_id, message_id, caption=None, parse_mode=None,disable_notification=None, reply_to_message_id=None, allow_sending_without_reply=None,timeout=None, protect_content=None, message_thread_id=None):
		data={'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
		if caption:data['caption'] = caption
		if parse_mode:data['parse_mode'] = parse_mode
		if disable_notification:data['disable_notification'] = disable_notification
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if timeout:data['timeout'] = timeout
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/copyMessage",json=data).json()
	def send_dice(self, chat_id,emoji=None, disable_notification=None, reply_to_message_id=None,timeout=None, allow_sending_without_reply=None, protect_content=None, message_thread_id=None):
		data={'chat_id': chat_id}
		if emoji:data['emoji'] = emoji
		if disable_notification:data['disable_notification'] = disable_notification
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if timeout:data['timeout'] = timeout
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendDice",json=data).json()
	def get_custom_emoji_stickers(self, custom_emoji_ids):
		data={'custom_emoji_ids': json.dumps(custom_emoji_ids)}
		return requests.post(f"{self.api}/getCustomEmojiStickers",json=data).json()
	def get_sticker_set(self, name):
		data={'name': name}
		return requests.post(f"{self.api}/getStickerSet",json=data).json()
	def set_sticker_position_in_set(self, sticker, position):
		data={'sticker': sticker, 'position': position}
		return requests.post(f"{self.api}/setStickerPositionInSet",json=data).json()
	def delete_sticker_from_set(self, sticker):
		data={'sticker': sticker}
		return requests.post(f"{self.api}/deleteStickerFromSet",json=data).json()
	def set_sticker_set_title(self,title,name):
		data={'name': name, 'title': title}
		return requests.post(f"{self.api}/setStickerSetTitle",json=data).json()
	def delete_sticker_set(self,name):
		data={'name': name}
		return requests.post(f"{self.api}/deleteStickerSet",json=data).json()
	def set_sticker_emoji_list(self, sticker, emoji_list):
		data= {'sticker': sticker, 'emoji_list': json.dumps(emoji_list)}
		return requests.post(f"{self.api}/setStickerEmojiList",json=data).json()
	def send_location(self,chat_id, latitude, longitude,live_period=None, reply_to_message_id=None, disable_notification=None, timeout=None, horizontal_accuracy=None, heading=None,proximity_alert_radius=None, allow_sending_without_reply=None, protect_content=None,message_thread_id=None):
		data={'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}
		if live_period:data['live_period'] = live_period
		if horizontal_accuracy:data['horizontal_accuracy'] = horizontal_accuracy
		if heading:data['heading'] = heading
		if proximity_alert_radius:data['proximity_alert_radius'] = proximity_alert_radius
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if disable_notification:data['disable_notification'] = disable_notification
		if timeout:data['timeout'] = timeout
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendLocation",json=data).json()
	def edit_message_live_location(self, latitude, longitude, chat_id=None, message_id=None,inline_message_id=None,timeout=None,horizontal_accuracy=None, heading=None, proximity_alert_radius=None):
		data={'latitude': latitude, 'longitude': longitude}
		if chat_id:data['chat_id'] = chat_id
		if message_id:data['message_id'] = message_id
		if horizontal_accuracy:data['horizontal_accuracy'] = horizontal_accuracy
		if heading:data['heading'] = heading
		if proximity_alert_radius:data['proximity_alert_radius'] = proximity_alert_radius
		if inline_message_id:data['inline_message_id'] = inline_message_id
		if timeout:data['timeout'] = timeout
		return requests.post(f"{self.api}/editMessageLiveLocation",json=data).json()
	def stop_message_live_location(self, chat_id=None, message_id=None,inline_message_id=None,reply_markup=None, timeout=None):
		data={}
		if chat_id:data['chat_id'] = chat_id
		if message_id:data['message_id'] = message_id
		if inline_message_id:data['inline_message_id'] = inline_message_id
		if timeout:data['timeout'] = timeout
		return requests.post(f"{self.api}/stopMessageLiveLocation",json=data).json()
	def send_venue(self, chat_id, latitude, longitude, title, address,foursquare_id=None, foursquare_type=None, disable_notification=None,reply_to_message_id=None,timeout=None,allow_sending_without_reply=None, google_place_id=None,google_place_type=None, protect_content=None, message_thread_id=None):
		data={'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude, 'title': title, 'address': address}
		if foursquare_id:data['foursquare_id'] = foursquare_id
		if foursquare_type:data['foursquare_type'] = foursquare_type
		if disable_notification:data['disable_notification'] = disable_notification
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if timeout:data['timeout'] = timeout
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if google_place_id:data['google_place_id'] = google_place_id
		if google_place_type:data['google_place_type'] = google_place_type
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendVenue",json=data).json()
	def send_contact(self, chat_id, phone_number, first_name, last_name=None, vcard=None,disable_notification=None, reply_to_message_id=None, timeout=None,allow_sending_without_reply=None, protect_content=None, message_thread_id=None):
		data={'chat_id': chat_id, 'phone_number': phone_number, 'first_name': first_name}
		if last_name:data['last_name'] = last_name
		if vcard:data['vcard'] = vcard
		if disable_notification:data['disable_notification'] = disable_notification
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if timeout:data['timeout'] = timeout
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendContact",json=data).json()
	def send_chat_action(self, chat_id, action, timeout=None, message_thread_id=None):
		data={'chat_id': chat_id, 'action': action}
		if timeout:data['timeout'] = timeout
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendChatAction",json=data).json()
	def send_video(self, chat_id, data, duration=None, caption=None, reply_to_message_id=None,parse_mode=None, supports_streaming=None, disable_notification=None, timeout=None,thumbnail=None, width=None, height=None, allow_sending_without_reply=None, protect_content=None,message_thread_id=None, has_spoiler=None):
		data={'chat_id': chat_id,'video': data}
		if duration:data['duration'] = duration
		if caption:data['caption'] = caption
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if parse_mode:data['parse_mode'] = parse_mode
		if supports_streaming:data['supports_streaming'] = supports_streaming
		if disable_notification:data['disable_notification'] = disable_notification
		if timeout:data['timeout'] = timeout
		if thumbnail: data['thumbnail'] = thumbnail
		if width:data['width'] = width
		if height:data['height'] = height
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		if has_spoiler:data['has_spoiler'] = has_spoiler
		return requests.post(f"{self.api}/sendVideo",json=data).json()
	def set_custom_emoji_sticker_set_thumbnail(self, name, custom_emoji_id=None):
		data={'name': name}
		if custom_emoji_id:data['custom_emoji_id'] = custom_emoji_id
		return requests.post(f"{self.api}/setCustomEmojiStickerSetThumbnail",json=data).json()
	def set_sticker_keywords(self, sticker, keywords=None):
		data={'sticker': sticker}
		if keywords:data['keywords'] = json.dumps(keywords)
		return requests.post(f"{self.api}/setStickerKeywords",json=data).json()
	def send_animation(self, chat_id, data, duration=None, caption=None, reply_to_message_id=None,parse_mode=None, disable_notification=None, timeout=None, thumbnail=None,allow_sending_without_reply=None, protect_content=None, width=None, height=None, message_thread_id=None,has_spoiler=None):
		data={'chat_id': chat_id,'animation': data}
		if duration:data['duration'] = duration
		if caption:data['caption'] = caption
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if parse_mode:data['parse_mode'] = parse_mode
		if disable_notification:data['disable_notification'] = disable_notification
		if timeout:data['timeout'] = timeout
		if thumbnail:data['thumbnail'] = thumbnail
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		if width:data['width'] = width
		if message_thread_id:data['message_thread_id'] = message_thread_id
		if has_spoiler:data['has_spoiler'] = has_spoiler
		return requests.post(f"{self.api}/sendAnimation",json=data).json()
	def send_voice(self,chat_id, voice, caption=None, duration=None, reply_to_message_id=None,parse_mode=None, disable_notification=None, timeout=None,allow_sending_without_reply=None, protect_content=None,message_thread_id=None):
		data={'chat_id': chat_id,'voice': voice}
		if duration:data['duration'] = duration
		if caption:data['caption'] = caption
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if parse_mode:data['parse_mode'] = parse_mode
		if disable_notification:data['disable_notification'] = disable_notification
		if timeout:data['timeout'] = timeout
		if message_thread_id:data['message_thread_id'] = message_thread_id
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		return requests.post(f"{self.api}/sendVoice",json=data).json()
	def send_video_note(self, chat_id, data, duration=None, length=None, reply_to_message_id=None,disable_notification=None, timeout=None, thumbnail=None, allow_sending_without_reply=None, protect_content=None,message_thread_id=None):
		data={'chat_id': chat_id,'video_note': data}
		if duration:data['duration'] = duration
		if length:data['length'] =length
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if disable_notification:data['disable_notification'] = disable_notification
		if timeout:data['timeout'] = timeout
		if  thumbnail:data['thumbnail'] = thumbnail
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendVideoNote",json=data).json()
	def send_audio(self, chat_id, audio, caption=None, duration=None, performer=None, title=None, reply_to_message_id=None,parse_mode=None, disable_notification=None, timeout=None, thumbnail=None,allow_sending_without_reply=None, protect_content=None, message_thread_id=None):
		data={'chat_id': chat_id,'audio': audio}
		if caption:data['caption'] = caption
		if duration:data['duration'] = duration
		if performer:data['performer'] = performer
		if title:data['title'] = title
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if parse_mode:data['parse_mode'] = parse_mode
		if disable_notification:data['disable_notification'] = disable_notification
		if timeout:data['timeout'] = timeout
		if thumbnail:data['thumbnail'] = thumbnail
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendAudio",json=data).json()
	def ban_chat_member(self, chat_id, user_id, until_date=None, revoke_messages=None):
		data={'chat_id': chat_id, 'user_id': user_id}
		if until_date:data['until_date']=until_date
		if revoke_messages:data['revoke_messages']=revoke_messages
		return requests.post(f"{self.api}/banChatMember",json=data).json()
	def unban_chat_member(self, chat_id, user_id, only_if_banned):
		data={'chat_id': chat_id, 'user_id': user_id}
		if only_if_banned:data['only_if_banned'] = only_if_banned
		return requests.post(f"{self.api}/unbanChatMember",json=data).json()
	def answer_callback_query(self, callback_query_id, text=None, show_alert=None, url=None, cache_time=None):
		data={'callback_query_id': callback_query_id}
		if text:data['text'] = text
		if show_alert:data['show_alert'] = show_alert
		if url:data['url'] = url
		if cache_time:data['cache_time'] = cache_time
		return requests.post(f"{self.api}/answerCallbackQuery",json=data).json()
	def answer_pre_checkout_query(self, pre_checkout_query_id, ok, error_message=None):
		data={'pre_checkout_query_id': pre_checkout_query_id, 'ok': ok}
		if error_message:data['error_message'] = error_message
		return requests.post(f"{self.api}/answerPreCheckoutQuery",json=data).json()
	def restrict_chat_member(self, chat_id, user_id, permissions, until_date=None,use_independent_chat_permissions=None):
		data={'chat_id': chat_id, 'user_id': user_id}
		if use_independent_chat_permissions:data['use_independent_chat_permissions'] = use_independent_chat_permissions
		if until_date:data['until_date'] = until_date
		return requests.post(f"{self.api}/restrictChatMember",json=data).json()
	def promote_chat_member(self, chat_id, user_id, can_change_info=None, can_post_messages=None,can_edit_messages=None, can_delete_messages=None, can_invite_users=None,can_restrict_members=None, can_pin_messages=None, can_promote_members=None,is_anonymous=None, can_manage_chat=None, can_manage_video_chats=None,can_manage_topics=None):
		data={'chat_id': chat_id, 'user_id': user_id}
		if can_change_info:data['can_change_info'] = can_change_info
		if can_post_messages:data['can_post_messages'] = can_post_messages
		if can_edit_messages:data['can_edit_messages'] = can_edit_messages
		if can_delete_messages:data['can_delete_messages'] = can_delete_messages
		if can_invite_users:data['can_invite_users'] = can_invite_users
		if can_restrict_members:data['can_restrict_members'] = can_restrict_members
		if can_pin_messages:data['can_pin_messages'] = can_pin_messages
		if can_promote_members:data['can_promote_members'] = can_promote_members
		if is_anonymous:data['is_anonymous'] = is_anonymous
		if can_manage_chat:data['can_manage_chat'] = can_manage_chat
		if can_manage_video_chats:data['can_manage_video_chats'] = can_manage_video_chats
		if can_manage_topics:data['can_manage_topics'] = can_manage_topics
		return requests.post(f"{self.api}/promoteChatMember",json=data).json()
	def set_chat_administrator_custom_title(self, chat_id, user_id, custom_title):
		data={'chat_id': chat_id, 'user_id': user_id, 'custom_title': custom_title}
		return requests.post(f"{self.api}/setChatAdministratorCustomTitle",json=data).json()
	def ban_chat_sender_chat(self, chat_id, sender_chat_id):
		data={'chat_id': chat_id, 'sender_chat_id': sender_chat_id}
		return requests.post(f"{self.api}/banChatSenderChat",json=data).json()
	def unban_chat_sender_chat(self, chat_id, sender_chat_id):
		data={'chat_id': chat_id, 'sender_chat_id': sender_chat_id}
		return requests.post(f"{self.api}/unbanChatSenderChat",json=data).json()
	def set_chat_permissions(self, chat_id, name, expire_date, member_limit, creates_join_request):
		data={'chat_id': chat_id,'expire_date':expire_date,'member_limit':member_limit,'creates_join_request':creates_join_request,'name':name}
		return requests.post(f"{self.api}/createChatInviteLink",json=data).json()
	def edit_chat_invite_link(self, chat_id, invite_link, name, expire_date, member_limit, creates_join_request):
		data={'chat_id': chat_id,'invite_link': invite_link,'expire_date':expire_date,'member_limit':member_limit,'creates_join_request':creates_join_request,'name':name}
		return requests.post(f"{self.api}/editChatInviteLink",json=data).json()
	def revoke_chat_invite_link(self,chat_id, invite_link):
		data={'chat_id': chat_id,'invite_link': invite_link}
		return requests.post(f"{self.api}/revokeChatInviteLink",json=data).json()
	def export_chat_invite_link(self, chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/exportChatInviteLink",json=data).json()
	def approve_chat_join_request(self, chat_id, user_id):
		data={'chat_id': chat_id,'user_id': user_id}
		return requests.post(f"{self.api}/approveChatJoinRequest",json=data).json()
	def decline_chat_join_request(self, chat_id, user_id):
		data={'chat_id': chat_id,'user_id': user_id}
		return requests.post(f"{self.api}/declineChatJoinRequest",json=data).json()
	def delete_chat_photo(self, chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/deleteChatPhoto",json=data).json()
	def set_chat_title(self, chat_id, title):
		data={'chat_id': chat_id, 'title': title}
		return requests.post(f"{self.api}/setChatTitle",json=data).json()
	def set_chat_title(self, chat_id, title):
		data= {'chat_id': chat_id, 'title': title}
		return requests.post(f"{self.api}/setChatTitle",json=data).json()
	def set_my_description(self, description=None, language_code=None):
		data={}
		if description:data['description'] = description
		if language_code:data['language_code'] = language_code
		return requests.post(f"{self.api}/setMyDescription",json=data).json()
	def get_my_description(self, language_code=None):
		data={}
		if language_code:data['language_code']=language_code
		return requests.post(f"{self.api}/getMyDescription",json=data).json()
	def answer_shipping_query(self, shipping_query_id, ok, error_message=None):
		data={'shipping_query_id': shipping_query_id, 'ok': ok}
		if error_message:data['error_message'] = error_message
		return requests.post(f"{self.api}/answerShippingQuery",json=data).json()
	def set_my_name(self, name=None, language_code=None):
		data={}
		if name:data['name'] = name
		if language_code:data['language_code'] = language_code
		return requests.post(f"{self.api}/setMyName",json=data).json()
	def get_my_name(self, language_code=None):
		data={}
		if language_code:data['language_code'] = language_code
		return requests.post(f"{self.api}/getMyName",json=data).json()
	def get_chat_menu_button(self, chat_id=None):
		data={}
		if chat_id:data['chat_id'] = chat_id
		return requests.post(f"{self.api}/getChatMenuButton",json=data).json()
	def get_my_default_administrator_rights(self, for_channels=None):
		data={}
		if for_channels:data['for_channels'] = for_channels
		return requests.post(f"{self.api}/getMyDefaultAdministratorRights",json=data).json()
	def set_chat_description(self, chat_id, description=None):
		data={'chat_id': chat_id}
		if description:data['description'] = description
		return requests.post(f"{self.api}/setChatDescription",json=data).json()
	def pin_chat_message(self, chat_id, message_id, disable_notification=None):
		data={'chat_id': chat_id, 'message_id': message_id}
		if disable_notification:data['disable_notification'] = disable_notification
		return requests.post(f"{self.api}/pinChatMessage",json=data).json()
	def unpin_chat_message(self, chat_id, message_id):
		data={'chat_id': chat_id, 'message_id': message_id}
		return requests.post(f"{self.api}/unpinChatMessage",json=data).json()
	def unpin_all_chat_messages(self, chat_id):
		data={'chat_id': chat_id}
		return requests.post(f"{self.api}/unpinAllChatMessages",json=data).json()
	def edit_message_text(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None,disable_web_page_preview=None):
		data={'text': text}
		if chat_id:data['chat_id'] = chat_id
		if message_id:data['message_id'] = message_id
		if inline_message_id:data['inline_message_id'] = inline_message_id
		if parse_mode:data['parse_mode'] = parse_mode
		if disable_web_page_preview:data['disable_web_page_preview'] = disable_web_page_preview
		return requests.post(f"{self.api}/editMessageText",json=data).json()
	def edit_message_caption(self, caption, chat_id=None, message_id=None, inline_message_id=None,parse_mode=None):
		data={'caption': caption}
		if chat_id:data['chat_id'] = chat_id
		if message_id:data['message_id'] = message_id
		if inline_message_id:data['inline_message_id'] = inline_message_id
		if parse_mode:data['parse_mode'] = parse_mode
		return requests.post(f"{self.api}/editMessageCaption",json=data).json()
	def delete_message(self, chat_id, message_id, timeout=None):
		data={'chat_id': chat_id, 'message_id': message_id}
		if timeout:data['timeout'] = timeout
		return requests.post(f"{self.api}/deleteMessage",json=data).json()
	def send_game(self, chat_id, game_short_name,disable_notification=None, reply_to_message_id=None, timeout=None,allow_sending_without_reply=None, protect_content=None, message_thread_id=None):
		data={'chat_id': chat_id, 'game_short_name': game_short_name}
		if disable_notification:data['disable_notification'] = disable_notification
		if reply_to_message_id:data['reply_to_message_id'] = reply_to_message_id
		if timeout:data['timeout'] = timeout
		if allow_sending_without_reply:data['allow_sending_without_reply'] = allow_sending_without_reply
		if protect_content:data['protect_content'] = protect_content
		if message_thread_id:data['message_thread_id'] = message_thread_id
		return requests.post(f"{self.api}/sendGame",json=data).json()
	def set_game_score(self, user_id, score, force=None, disable_edit_message=None, chat_id=None, message_id=None,inline_message_id=None):
		data={'user_id': user_id, 'score': score}
		if force:data['force'] = force
		if chat_id:data['chat_id'] = chat_id
		if message_id:data['message_id'] = message_id
		if inline_message_id:data['inline_message_id'] = inline_message_id
		if disable_edit_message:data['disable_edit_message'] = disable_edit_message
		return requests.post(f"{self.api}/sendGameScore",json=data).json()
	def get_game_high_scores(self, user_id, chat_id=None, message_id=None, inline_message_id=None):
		data={'user_id': user_id}
		if chat_id:data['chat_id'] = chat_id
		if message_id:data['message_id'] = message_id
		if inline_message_id:data['inline_message_id'] = inline_message_id
		return requests.post(f"{self.api}/getGameHighScores",json=data).json()