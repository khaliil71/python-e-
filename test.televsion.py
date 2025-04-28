class Television:
    

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        
        self.__status = not self.__status

    def mute(self) -> None:
        
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        
        if self.__status:
            self.__channel = Television.MIN_CHANNEL if self.__channel == Television.MAX_CHANNEL else self.__channel + 1

    def channel_down(self) -> None:
        
        if self.__status:
            self.__channel = Television.MAX_CHANNEL if self.__channel == Television.MIN_CHANNEL else self.__channel - 1

    def volume_up(self) -> None:
        
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = 1  
            elif self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = 0  
            elif self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        
        display_volume = 0 if (self.__muted and self.__status) else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"
