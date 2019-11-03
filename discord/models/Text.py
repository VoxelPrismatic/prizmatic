class Text:
    """
    >> REPRESENTS A MESSAGE
            id [int   ] - The Message ID
    channel_id [int   ] - The Channel ID
      guild_id [int?  ] - The Guild ID, None if in DMs
        author [Player] - The Player that sent the message
          text [str   ] - The message content
          type [int   ] - The message type [call, regular, etc]
   at_everyone [bool  ] - Whether the message pings everyone
        pinned [bool  ] - Whether or not the message was pinned
    webhook_id [int?  ] - The ID of the webhook that sent it,
                        - None if it wasnt sent by a webhook
                        
    
         pings [list(Player)     ] - The list of `Player`s that got pinged
    role_pings [list(Role)       ] - The list of `Role`s that got pinged
 channel_pings [list(ChannelBase)] - The list of `ChannelBase`s that got pinged
   attachments [list(Attachment) ] - The list of `Attachment`s sent with the message
        embeds [list(Embed)      ] - The list of `Embed`s that the message has
     reactions [list(Reaction)   ] - The list of `Reaction`s that the message has
         nonce [Snow?            ] - Whether or not the message was sent
    """
    def __init__
