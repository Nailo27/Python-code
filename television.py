class Television:
    MIN_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3

    def __init__(self):
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status

    def mute(self):
        """
        When the Television is on, the mute status is changed.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        When the power is on, the channel is increased by one.
        if it is at max, go to min.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
            While Television is on, decrease the channel by 1.
             If at min, go to max.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
            While Television is on, increase volume by 1. If at max, stay.
            If muted, unmute then continue.
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self):
        """
            While Television is on, decrease volume by 1. If at min, stay.
            If muted, unmute then continue.
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self):
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
