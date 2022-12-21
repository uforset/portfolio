package com.circle.foodstagram.chat.controller;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import com.circle.foodstagram.chat.model.dao.ChatRoomDao;
import com.circle.foodstagram.chat.model.service.ChatService;
import com.circle.foodstagram.chat.model.vo.ChatMessage;
import com.circle.foodstagram.chat.model.vo.ChatRoom;
import com.circle.foodstagram.chat.model.vo.ChatRoomJoin;
import com.circle.foodstagram.member.model.vo.Member;
import com.circle.foodstagram.member.service.MemberService;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j;
import net.sf.json.JSONObject;

@Controller
@RequiredArgsConstructor
@RequestMapping(value = "/chat")
@Log4j
public class RoomController {
	

	@Autowired
	private ChatService chatService;
	
	@Autowired
	private MemberService memberService;
	/*
	//채팅방 목록 조회
    @GetMapping(value = "/rooms")
    public ModelAndView rooms(){

        //log.info("# All Chat Rooms");
        ModelAndView mv = new ModelAndView("chat/rooms");
        log.info(chatRoomService.findAllRooms().toString());
        mv.addObject("list", chatRoomService.findAllRooms());


        return mv;
    }
	*/
    /*
    //채팅방 개설
    @PostMapping(value = "/room")
    public String create(@RequestParam String name, RedirectAttributes rttr){


        log.info("# Create Chat Room , name: " + name);
        rttr.addFlashAttribute("roomName", chatRoomService.createChatRoomDTO(name));
        return "redirect:/chat/rooms";
    }
     */
    
    /*
    //채팅방 조회
    @GetMapping("/room")
    public String getRoom(String roomId, Model model){

    	//log.info("# get Chat Room, roomID : " + roomId);
    	log.info("# get Chat Room, roomID : " + roomId);
    	log.info("# get Chat chatRoomService.findRoomById(roomId), id? : " + chatRoomService.findRoomById(roomId));
    	//그냥 채팅방 정보(ChatRoom vo) 담는거임 어느채팅방 들어갔는지
        model.addAttribute("room", chatRoomService.findRoomById(roomId));
        
        return "chat/room";
    }
    */
    
	
    // new
    //채팅방 개설
    @PostMapping(value = "/room")
    @ResponseBody
    public String create(@RequestParam List<String> userList,
    		HttpSession session, 
    		RedirectAttributes rttr,
    		Model model){
    	Member loginMember = (Member) session.getAttribute("loginMember");
    	if(loginMember == null) {
    		model.addAttribute("message", "로그인상태가 아닙니다.");
    		return "common/error";
    	}
    	String myId =loginMember.getUserid();
    	
    	log.info(userList);
    	
    	//List<String> userList = Arrays.asList(userList2);
    	//DM초대하기(채팅방만들기)
    	//사용자가 유저를 검색해서 선택하고 초대함(한명 또는 여러명)
    	//채팅방을 생성하고, 그채팅방 id를 이용해 채팅방참여자DB에 저장.
    	
    	// 랜덤UUID생성후 DB에 저장함
    	
    	String uuid = UUID.randomUUID().toString();
    	ChatRoom chatRoom = new ChatRoom();
    	chatRoom.setChat_room_id(uuid);
    	chatRoom.setTitle("emp");
    	int size = userList.size();
    	
    	chatService.createChatRoom(chatRoom);
    	//성공시 진행
    	
    	//초대자들(본인포함) 채팅방참여DB에 저장
    	if (!userList.contains(myId)) { // 내 아이디도 db에 저장되어야하므로 없으면 추가해줌.
    		userList.add(myId);
    	}
    	
    	log.info("참여자 목록 uuid : " + uuid);
    	for(String userid : userList) {
    		log.info( "userid : "+ userid);
    	}
    	
    	for(String userid : userList) {
    		ChatRoomJoin join = new ChatRoomJoin();
    		join.setChat_room_id(uuid);
    		join.setUserid(userid);
    		
    		chatService.insertChatRoomJoin(join);
    	}
    	
        log.info("# Create Chat Room , name: " + chatRoom.getChat_room_id());
        //rttr.addFlashAttribute("roomName", chatRoom.getTitle());
        JsonObject senjson = new JsonObject();
        senjson.addProperty("uuid", uuid);
 
        return senjson.toString();
    }
    
    
    // 채팅방 들어감 방목록
    @GetMapping("/room")
    public String getRoom(String roomId, HttpSession session, Model model){

    	Member loginMember = (Member) session.getAttribute("loginMember");
    	if(loginMember == null) {
    		model.addAttribute("message", "로그인상태가 아닙니다.");
    		return "common/error";
    	}
    	String myId =loginMember.getUserid();
    	
    	List<ChatRoom> list = chatService.findAllMyRooms(myId);
    	
    	for(ChatRoom cr : list) {
    		if (!cr.getTitle().equals("emp"))
        		continue;
    		List<ChatRoomJoin> crjList = cr.getParticipants();
        	// crjList => 참여자수, 참여자들 알수있음
        	int size = crjList.size();
        	ArrayList<String> userArray = new ArrayList<String>();
        	for(ChatRoomJoin crj : crjList) {
        		userArray.add(crj.getUserid());
        	}
        	log.info(cr.getChat_room_id()+"번 방 참여자들 : ");
        	log.info(userArray);
        	userArray.remove(loginMember.getUserid()); // 쉽게 제목을보여주기위해 자기자신은 제외함
        	
        	if(size == 1) { // 인원이 한명이면 혼자있는 채팅방임
        		cr.setTitle(loginMember.getUsername()); 
        	} else if (size == 2) { // 1:1채팅방임
        		cr.setTitle(memberService.selectMember(userArray.get(0)).getUsername());
        	}else if (size < 5) { // 3명까지
        		String title="";
        		for(String id :userArray) {
        			title += memberService.selectMember(id).getUsername()+" ";
        		}
        		title = title.trim().replaceAll(" ", ", ") + "님";
        		cr.setTitle(title);
        	} else { // 4명이상
        		String title="";
        		for(int i=0; i<3; i++) {
        			title += memberService.selectMember(userArray.get(i)).getUsername()+" ";
        		}
        		title = title.trim().replaceAll(" ", ", ") + "님 외 " + (size-4) + "명";
        		cr.setTitle(title);
        	}
        }
        

    	log.info("# get Chat Room, roomID : " + roomId);
    	//그냥 채팅방 정보(ChatRoom vo) 담는거임 어느채팅방 들어갔는지
    	ChatRoom selectedRoom = chatService.findRoomByUUId(roomId);
    	
    	for(ChatRoom cr : list) { // find안하고 해도되긴함..
    		if(cr.getChat_room_id().equals(roomId)) {
    			selectedRoom.setTitle(cr.getTitle());
    			List<ChatRoomJoin> participants = cr.getParticipants();
    			selectedRoom.setParticipants(participants);

    			break;
    		}
    	}
    
    	List<ChatMessage> mlist = chatService.getChatRoomMessage(selectedRoom.getChat_room_id());
    	//스크롤 페이징 하려면 수정필요.
    	//시간순으로 정렬해줘서 가져옴.
    	log.info("방에서 가져온 메세지 확ㅇ니!!!!");
    	log.info(mlist);
    	
    	model.addAttribute("list", list);
    	model.addAttribute("selectedRoom", selectedRoom);
        model.addAttribute("mlist", mlist);
    	
        return "chat/testRoom";
    }
    
    //채팅방 목록 조회
    @GetMapping(value = "/rooms")
    public String roomList(HttpSession session, Model model){

    	Member loginMember = (Member) session.getAttribute("loginMember");
    	if(loginMember == null) {
    		model.addAttribute("message", "로그인상태가 아닙니다.");
    		return "common/error";
    	}
    	String myId =loginMember.getUserid();
        //log.info("# All Chat Rooms");
        //ModelAndView mv = new ModelAndView("chat/rooms");
        //log.info(chatRoomService.findAllRooms().toString());
        //mv.addObject("list", chatRoomService.findAllRooms());
        List<ChatRoom> list = chatService.findAllMyRooms(myId);
        //위에 메소드로 각방의 초대자들까지 셋팅됨.
        
        
        
        log.info(list.toString());
        for(ChatRoom cr : list) {
        	List<ChatRoomJoin> crjList = cr.getParticipants();
        	// crjList => 참여자수, 참여자들 알수있음
        	if (!cr.getTitle().equals("emp"))
        		continue;
        	
        	int size = crjList.size();
        	ArrayList<String> userArray = new ArrayList<String>();
        	for(ChatRoomJoin crj : crjList) {
        		userArray.add(crj.getUserid());
        	}
        	log.info(cr.getChat_room_id()+"번 방 참여자들 : ");
        	log.info(userArray);
        	userArray.remove(loginMember.getUserid()); // 쉽게 제목을보여주기위해 자기자신은 제외함
        	
        	if(size == 1) { // 인원이 한명이면 혼자있는 채팅방임
        		cr.setTitle(loginMember.getUsername()); 
        	} else if (size == 2) { // 1:1채팅방임
        		cr.setTitle(memberService.selectMember(userArray.get(0)).getUsername());
        	}else if (size < 5) { // 3명까지
        		String title="";
        		for(String id :userArray) {
        			title += memberService.selectMember(id).getUsername()+" ";
        		}
        		title = title.trim().replaceAll(" ", ", ") + "님";
        		cr.setTitle(title);
        	} else { // 4명이상
        		String title="";
        		for(int i=0; i<3; i++) {
        			title += memberService.selectMember(userArray.get(i)).getUsername()+" ";
        		}
        		title = title.trim().replaceAll(" ", ", ") + "님 외 " + (size-4) + "명";
        		cr.setTitle(title);
        	}
        }
        
        
        model.addAttribute("list", list);

        return "chat/testRooms";
    }
    
    @PostMapping("getMembers.do")
    @ResponseBody
    public String getMembersMethod(@RequestParam String keyword) {

    	Gson gson = new Gson();
    	ArrayList<Member> mlist = memberService.selectSearchUseridUsername(keyword);
    	log.info(gson.toJson(mlist));
    	return gson.toJson(mlist);
    }
    
    
    @GetMapping("getNextChat.do/{page}")
    @ResponseBody
    public String getPageChatMessageMethod(
    		@PathVariable(name = "page") int page,
    		@RequestParam String id) {
    	
    	Gson gson = new Gson();
    	Map<String,Object> map = new HashMap<String,Object>();
    	
    	int size = 20;
    	
    	map.put("page", page);
    	map.put("size", size);
    	map.put("id", id);
    	
    	
    	List<ChatMessage> mlist = chatService.getChatMessageRowLimitingClausePaging(map);
    	//스크롤 페이징 하려면 수정필요.
    	//시간순으로 정렬해줘서 가져옴.
    	log.info("방에서 가져온 메세지 확ㅇ니!!!!");
    	log.info("사이즈확인 20개여야되는데" + mlist.size());
    	log.info(mlist);
    	
    	log.info(gson.toJson(mlist));
    	return gson.toJson(mlist);
    }
    
    @PostMapping("deleteMessage.do")
    @ResponseBody
    public String deleteMessageMethod(
    		@RequestParam int cm_no) {

    	
    	JsonObject sendjson = new JsonObject();
    	
    	if( chatService.deleteMessage(cm_no) > 0 ) {
    		log.info("삭제성공");
    		sendjson.addProperty("status", "success");
    	} else {
    		sendjson.addProperty("status", "failed");
    	}
    	
    	
    	return sendjson.toString();
    }
    
    @PostMapping("roomTitleEdit.do")
    @ResponseBody
    public String roomTitleEditMethod(
    		ChatRoom room) {
    	JsonObject sendjson = new JsonObject();
    	
    	if( chatService.updateRoomTitle(room) > 0) {
    		log.info("수정성공");
			sendjson.addProperty("status", "success");
		} else {
			sendjson.addProperty("status", "failed");
		}
    	return sendjson.toString();
    }
    
    @PostMapping("leaveChatRoom.do")
    @ResponseBody
    public String leaveChatRoomMethod(
    		@RequestParam String userid,
    		@RequestParam String chat_room_id) {
    	JsonObject sendjson = new JsonObject();
    	
    	Map<String,Object> map = new HashMap<String,Object>();
    	map.put("userid", userid);
    	map.put("chat_room_id", chat_room_id);
    	
    	if( chatService.deleteChatRoomJoin(map) > 0) {
    		log.info("탈출성공ㅜ");
			sendjson.addProperty("status", "success");
		} else {
			sendjson.addProperty("status", "failed");
		}
    	
    	return sendjson.toString();
    }
}
