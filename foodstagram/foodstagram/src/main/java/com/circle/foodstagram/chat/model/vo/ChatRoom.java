package com.circle.foodstagram.chat.model.vo;

import java.io.Serializable;
import java.util.Date;
import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;


@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class ChatRoom implements Serializable {

	private static final long serialVersionUID = -2181919565975833687L;
	private String chat_room_id;		// 채팅방 No
	private String title;	// 채팅방 제목
	private Date create_date; // 생성일
	private Date renewal_date; // 갱신일
	
	private List<ChatRoomJoin> participants;
}
