    .file  "main.java"
__SREG__ = 0x3f
__SP_H__ = 0x3e
__SP_L__ = 0x3d
__tmp_reg__ = 0
__zero_reg__ = 1
    .global __do_copy_data
    .global __do_clear_bss
    .text
.global main
    .type   main, @function
main:
    push r29
    push r28
    in r28,__SP_L__
    in r29,__SP_H__
/* prologue: function */
    call _Z18MeggyJrSimpleSetupv 
    /* Need to call this so that the meggy library gets set up */
checkDown:    
    call	_Z16CheckButtonsDownv
    lds		r24, Button_Down
    
    tst		r24
    breq	MJ_L1
    
checkUp:
    call	Z16CheckButtonsDownv
    lds		r24, Button_Up
    
    tst		r24
    breq	MJ_L2
    
jmp checkDown 
    
MJ_L1:
    ldi		r24, lo8(3)
    ldi		r22, lo8(0)
    ldi		r20, lo8(1)
    call	_Z6DrawPxhhh
    call	_Z12DisplaySlatev
    jmp		checkUp
    
MJ_L2:
    ldi		r24, lo8(3)
    ldi		r22, lo8(7)
    ldi		r20, lo8(5)
    call	_Z6DrawPxhhh
    call	_Z12DisplaySlatev
    jmp		checkDown